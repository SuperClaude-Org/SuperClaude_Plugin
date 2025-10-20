import datetime
import os
import platform
import shutil
import subprocess
import sys
from pathlib import Path

# --- Configuration ---
PACKAGE_NAME = "superclaude" # Used mainly for scanning native/legacy files
COMMAND_PACKAGES = {
    'pip': 'superclaude',
    'pipx': 'superclaude',
    'uv': 'superclaude',
    'npm': '@bifrost_inc/superclaude'
}
# Safer list of V3 legacy file patterns
V3_LEGACY_PATTERNS = ["CLAUDE.md", "TASK.md", "KNOWLEDGE.md", "PLANNING.md", "commands/"]
# Claude Code files to protect from deletion
PROTECTED_FILES = [".claude.json", "settings.json", "settings.local.json", "credentials.json"]


# --- Color Settings for Terminal Output ---
class Colors:
    """ANSI color codes for terminal output"""
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_color(message, color):
    """Prints a message in the specified color."""
    # Color codes don't work well in basic Windows CMD, but do in modern terminals like Windows Terminal.
    # A simple check for a modern terminal environment variable.
    if platform.system() == "Windows" and 'WT_SESSION' not in os.environ:
        print(message)
    else:
        print(f"{color}{message}{Colors.ENDC}")

# --- Helper Functions ---
def command_exists(cmd):
    """Checks if a command exists on the system's PATH."""
    return shutil.which(cmd) is not None

def run_command(command, capture=True):
    """Runs a specified command in a subprocess and returns the result."""
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=capture,
            text=True,
            encoding='utf-8',
            check=False
        )
        return result
    except FileNotFoundError:
        # This can happen if the command itself (e.g., 'pip') is not found.
        return None
    except Exception as e:
        print_color(f"  An unexpected error occurred while running command: {e}", Colors.FAIL)
        return None

# --- Conflict Detection Module ---

def check_installation(manager, package_name):
    """Checks if a package is installed using a specific package manager."""
    if not command_exists(manager):
        return False
    check_command = {
        'pip': f"pip show {package_name}",
        'pipx': "pipx list",
        'uv': f"uv pip show {package_name}",
        'npm': f"npm list -g {package_name}"
    }.get(manager)

    result = run_command(check_command)

    if result and result.returncode == 0 and result.stdout:
        # pipx lists all packages, so we need to check if our package is in the output.
        if manager == 'pipx':
            return package_name in result.stdout
        # npm can return an empty stdout even on success, so we check for the package name.
        if manager == 'npm':
            return package_name in result.stdout
        return True
    return False

def find_conflicting_installations():
    """Detects all potentially conflicting installations and returns a list."""
    conflicts = []
    for manager, package_name in COMMAND_PACKAGES.items():
        if check_installation(manager, package_name):
            conflicts.append(manager)
    return conflicts

# --- Uninstallation Process ---

def uninstall_package(manager):
    """Uninstalls the package from the specified package manager."""
    package_name = COMMAND_PACKAGES[manager]
    print_color(f"\n--- Uninstalling '{package_name}' from {manager.upper()} ---", Colors.HEADER)

    uninstall_command = {
        'pip': f"pip uninstall -y {package_name}",
        'pipx': f"pipx uninstall {package_name}",
        'uv': f"uv pip uninstall -y {package_name}",
        'npm': f"npm uninstall -g {package_name}"
    }.get(manager)

    run_command(uninstall_command, capture=False)

    print(f"\n  Verifying uninstallation...")
    if not check_installation(manager, package_name):
        print_color(f"  ✅ Successfully uninstalled '{package_name}' from {manager}.", Colors.OKGREEN)
    else:
        print_color(f"  ❌ Failed to uninstall '{package_name}' from {manager}.", Colors.FAIL)
        print_color(f"     Please try running '{uninstall_command}' manually.", Colors.FAIL)

# --- Native Plugin and Legacy File Handling ---

def handle_native_plugins_and_legacy_files():
    """Detects native plugin directories and V3 legacy files, then guides the cleanup."""
    print_color("\n--- Checking for Native Plugins and V3 Legacy Files ---", Colors.HEADER)

    home_dir = Path.home()
    claude_dir = home_dir / ".claude"
    current_dir = Path.cwd()

    paths_to_scan = {"SuperClaude config directory": claude_dir, "Current directory": current_dir}
    files_to_remove = []

    for description, scan_path in paths_to_scan.items():
        if not scan_path.exists(): continue
        print_color(f"\n  🔍 Scanning {description} ({scan_path})...", Colors.OKCYAN)

        for pattern in V3_LEGACY_PATTERNS:
            # Handle directory patterns (ending in '/')
            if pattern.endswith('/'):
                path = scan_path / pattern[:-1]
                if path.is_dir():
                    files_to_remove.append(path)
                    # Also add all contents of the directory for explicit removal
                    files_to_remove.extend(p for p in path.rglob("*"))
            else: # Handle file patterns
                for path in scan_path.glob(pattern):
                    if path.is_file() and path.name not in PROTECTED_FILES:
                        files_to_remove.append(path)

    # If anything inside .claude is marked for deletion, mark the whole directory for deletion
    if claude_dir.exists() and any(p == claude_dir or p.is_relative_to(claude_dir) for p in files_to_remove):
        files_to_remove.append(claude_dir)

    if not files_to_remove:
        print_color("  No native plugins or legacy files found to clean up.", Colors.OKGREEN)
        return

    # Deduplicate and sort the list of paths
    files_to_remove = sorted(list(set(files_to_remove)))
    print_color("\n  The following files and directories have been detected for cleanup:", Colors.WARNING)
    for path in files_to_remove:
        try:
            # Make paths more readable by showing them relative to home
            display_path = path.relative_to(home_dir)
            print(f"    -> ~/{display_path}")
        except ValueError:
            # The path is outside the home directory
            print(f"    -> {path}")

    non_interactive = '-y' in sys.argv or '--yes' in sys.argv
    if not non_interactive:
        try:
            answer = input(f"\n{Colors.WARNING}  Do you want to back up and delete these items? (y/n): {Colors.ENDC}").lower().strip()
            if answer != 'y':
                print("\n  Skipping cleanup of native files.")
                return
        except (KeyboardInterrupt, EOFError):
            print("\n  Cleanup skipped.")
            return

    backup_successful = create_backup_strategy(files_to_remove, home_dir, claude_dir)

    if backup_successful:
        print("\n  Backup complete. Starting file deletion...")
        # Iterate backwards to delete files before their parent directories
        for path in reversed(files_to_remove):
            try:
                if path.is_file():
                    path.unlink()
                    print(f"    🗑️  Deleted: {path}")
                elif path.is_dir():
                    # Check if the directory is now empty before deleting
                    if not any(item.is_relative_to(path) for item in files_to_remove if item != path):
                       shutil.rmtree(path)
                       print(f"    🗑️  Deleted directory: {path}")

            except Exception as e:
                print_color(f"  ❌ Error: Failed to delete {path} - {e}", Colors.FAIL)
        print_color("\n  ✅ File cleanup complete.", Colors.OKGREEN)
    else:
        print_color("\n  Backup failed. No files were deleted.", Colors.FAIL)

def create_backup_strategy(files_to_backup, home_dir, claude_dir):
    """Executes a hybrid strategy combining official and manual backups."""
    claude_dir_files_exist = any(p == claude_dir or p.is_relative_to(claude_dir) for p in files_to_backup)
    other_files = [p for p in files_to_backup if not (p == claude_dir or p.is_relative_to(claude_dir))]

    official_backup_done = False
    # Attempt official backup only if the .claude directory is targeted
    if claude_dir_files_exist and command_exists("SuperClaude"):
        print_color("\n  Attempting to back up ~/.claude using the official backup command...", Colors.OKBLUE)
        result = run_command("SuperClaude backup --create", capture=False)
        if result and result.returncode == 0:
            print_color("  ✅ Official backup created successfully.", Colors.OKGREEN)
            official_backup_done = True
        else:
            print_color("  ❌ Official backup command failed. Falling back to manual backup.", Colors.FAIL)

    files_for_manual_backup = []
    # If official backup failed or wasn't applicable, add .claude files to manual backup list
    if not official_backup_done and claude_dir_files_exist:
         files_for_manual_backup.extend([p for p in files_to_backup if p == claude_dir or p.is_relative_to(claude_dir)])

    # Always add files outside the .claude directory to the manual backup list
    files_for_manual_backup.extend(other_files)
    if not files_for_manual_backup: return True

    return create_manual_zip_backup(list(set(files_for_manual_backup)), home_dir)

def create_manual_zip_backup(paths_to_backup, backup_dir):
    """Backs up a list of specified paths into a single ZIP file."""
    print_color("\n  Creating a manual ZIP backup...", Colors.OKBLUE)
    backup_base_name = f"{PACKAGE_NAME}_cleanup_backup_{datetime.datetime.now().strftime('%Y%m%d-%H%M%S')}"
    backup_archive_path = backup_dir / backup_base_name
    temp_backup_dir = backup_dir / f"temp_{backup_base_name}"

    try:
        temp_backup_dir.mkdir(exist_ok=True)
        print(f"  Creating backup...")

        for path in paths_to_backup:
            dest_path_segment = None
            try:
                # Store files with a path relative to home to preserve structure
                dest_path_segment = path.relative_to(Path.home())
            except ValueError:
                # Handle files outside of home directory
                dest_path_segment = Path("__external_paths__") / str(path).lstrip(os.path.sep)

            dest_path = temp_backup_dir / dest_path_segment
            dest_path.parent.mkdir(parents=True, exist_ok=True)

            if path.is_dir():
                shutil.copytree(path, dest_path, dirs_exist_ok=True)
            elif path.is_file():
                shutil.copy2(path, dest_path)

        shutil.make_archive(str(backup_archive_path), 'zip', str(temp_backup_dir))
        print_color(f"  ✅ Manual backup created successfully: {backup_archive_path}.zip", Colors.OKGREEN)
        return True
    except Exception as e:
        print_color(f"  ❌ An error occurred during manual backup: {e}", Colors.FAIL)
        return False
    finally:
        # Clean up the temporary directory
        if temp_backup_dir.exists():
            shutil.rmtree(temp_backup_dir)

def main():
    """Main function for the script."""
    print_color("=====================================================", Colors.BOLD)
    print_color(f"=== {PACKAGE_NAME.capitalize()} Cleanup Script (V4 Compatible) ===", Colors.BOLD)
    print_color("=====================================================", Colors.BOLD)
    print("This script will detect and attempt to clean up all SuperClaude installations and V3 legacy files from your system.")

    non_interactive = '-y' in sys.argv or '--yes' in sys.argv

    print_color("\n--- Checking for conflicting CLI installations ---", Colors.HEADER)
    conflicting_installations = find_conflicting_installations()
    if not conflicting_installations:
        print_color("  No conflicting CLI installations found.", Colors.OKCYAN)
    else:
        print_color(f"  Found conflicting installations from: {', '.join(conflicting_installations)}", Colors.WARNING)
        should_uninstall = non_interactive
        if not non_interactive:
            try:
                answer = input(f"{Colors.WARNING}  Do you want to uninstall them? (y/n): {Colors.ENDC}").lower().strip()
                if answer == 'y': should_uninstall = True
            except (KeyboardInterrupt, EOFError):
                print("\n  Uninstallation skipped.")
        if should_uninstall:
            for manager in conflicting_installations:
                uninstall_package(manager)

    handle_native_plugins_and_legacy_files()
    print_color("\n--- Cleanup Finished ---", Colors.HEADER)
    print_color("All checks are complete.", Colors.OKGREEN)
    print("You are now ready for a clean installation of the official plugin.")

if __name__ == "__main__":
    main()
