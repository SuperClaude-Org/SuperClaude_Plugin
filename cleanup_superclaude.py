
import datetime
import os
import platform
import shutil
import subprocess
import sys
from pathlib import Path

# --- 設定 ---
PACKAGE_NAME = "superclaude" # 主にネイティブ/遺物ファイルのスキャンに使用
COMMAND_PACKAGES = {
    'pip': 'superclaude',
    'pipx': 'superclaude',
    'uv': 'superclaude',
    'npm': '@bifrost_inc/superclaude'
}
# V3の遺物ファイルパターン（より安全なリスト）
V3_LEGACY_PATTERNS = ["CLAUDE.md", "TASK.md", "KNOWLEDGE.md", "PLANNING.md", "commands/"]
# Claude Codeの保護対象ファイル
PROTECTED_FILES = [".claude.json", "settings.json", "settings.local.json", "credentials.json"]


# --- ターミナル出力用の色設定 ---
class Colors:
    """ターミナル出力用のANSIカラーコード"""
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
    """色付きでメッセージを印刷する"""
    if platform.system() == "Windows" and 'WT_SESSION' not in os.environ:
        print(message)
    else:
        print(f"{color}{message}{Colors.ENDC}")

# --- ヘルパー関数 ---
def command_exists(cmd):
    """指定されたコマンドがシステムのPATHに存在するか確認する"""
    return shutil.which(cmd) is not None

def run_command(command, capture=True):
    """指定されたコマンドをサブプロセスで実行し、結果を返す"""
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
        return None
    except Exception as e:
        print_color(f"  コマンド実行中に予期せぬエラーが発生しました: {e}", Colors.FAIL)
        return None

# --- 競合検知モジュール ---

def check_installation(manager, package_name):
    """指定されたパッケージマネージャーでパッケージがインストールされているか確認する"""
    if not command_exists(manager):
        return False
    check_command = {
        'pip': f"pip show {package_name}", 'pipx': "pipx list",
        'uv': f"uv pip show {package_name}", 'npm': f"npm list -g {package_name}"
    }.get(manager)
    result = run_command(check_command)
    if result and result.returncode == 0 and result.stdout:
        # pipxは全パッケージをリストするため、出力にパッケージ名が含まれるか確認
        if manager == 'pipx':
            return package_name in result.stdout
        # npmは空のstdoutを返すことがあるので、stdoutの内容もチェック
        if manager == 'npm':
            return package_name in result.stdout
        return True
    return False

def find_conflicting_installations():
    """競合する可能性のある全てのインストールを検知し、リストを返す"""
    conflicts = []
    for manager, package_name in COMMAND_PACKAGES.items():
        if check_installation(manager, package_name):
            conflicts.append(manager)
    return conflicts

# --- アンインストール処理 ---

def uninstall_package(manager):
    """指定されたパッケージマネージャーからパッケージをアンインストールする"""
    package_name = COMMAND_PACKAGES[manager]
    print_color(f"\n--- {manager.upper()} から '{package_name}' をアンインストールします ---", Colors.HEADER)

    uninstall_command = {
        'pip': f"pip uninstall -y {package_name}",
        'pipx': f"pipx uninstall {package_name}",
        'uv': f"uv pip uninstall -y {package_name}",
        'npm': f"npm uninstall -g {package_name}"
    }.get(manager)

    run_command(uninstall_command, capture=False)

    print(f"\n  アンインストールが成功したか再確認しています...")
    if not check_installation(manager, package_name):
        print_color(f"  ✅ {manager} から '{package_name}' を正常にアンインストールしました。", Colors.OKGREEN)
    else:
        print_color(f"  ❌ {manager} から '{package_name}' のアンインストールに失敗した可能性があります。", Colors.FAIL)
        print_color(f"     手動で '{uninstall_command}' を実行してみてください。", Colors.FAIL)

# --- ネイティブプラグインと遺物ファイルの処理 ---

def handle_native_plugins_and_legacy_files():
    """ネイティブプラグインのディレクトリとV3の遺物ファイルを検出し、クリーンアップを案内する"""
    print_color("\n--- ネイティブプラグインとV3遺物ファイルの確認 ---", Colors.HEADER)

    home_dir = Path.home()
    claude_dir = home_dir / ".claude"
    current_dir = Path.cwd()

    paths_to_scan = {"SuperClaude設定ディレクトリ": claude_dir, "カレントディレクトリ": current_dir}
    files_to_remove = []

    for description, scan_path in paths_to_scan.items():
        if not scan_path.exists(): continue
        print_color(f"\n  🔍 {description} ({scan_path}) をスキャンしています...", Colors.OKCYAN)

        for pattern in V3_LEGACY_PATTERNS:
            if pattern.endswith('/'):
                path = scan_path / pattern[:-1]
                if path.is_dir():
                    files_to_remove.append(path)
                    files_to_remove.extend(p for p in path.rglob("*"))
            else:
                for path in scan_path.glob(pattern):
                    if path.is_file() and path.name not in PROTECTED_FILES:
                        files_to_remove.append(path)

    if claude_dir.exists() and any(p == claude_dir or p.is_relative_to(claude_dir) for p in files_to_remove):
        files_to_remove.append(claude_dir)

    if not files_to_remove:
        print_color("  クリーンアップ対象のネイティブプラグインや遺物ファイルは見つかりませんでした。", Colors.OKGREEN)
        return

    files_to_remove = sorted(list(set(files_to_remove)))
    print_color("\n  以下のファイルとディレクトリがクリーンアップ対象として検出されました：", Colors.WARNING)
    for path in files_to_remove:
        try:
            display_path = path.relative_to(home_dir)
            print(f"    -> ~/{display_path}")
        except ValueError:
            print(f"    -> {path}")

    non_interactive = '-y' in sys.argv or '--yes' in sys.argv
    if not non_interactive:
        try:
            answer = input(f"\n{Colors.WARNING}  これらをバックアップして削除しますか？ (y/n): {Colors.ENDC}").lower().strip()
            if answer != 'y':
                print("\n  クリーンアップをスキップします。")
                return
        except (KeyboardInterrupt, EOFError):
            print("\n  クリーンアップをスキップします。")
            return

    backup_successful = create_backup_strategy(files_to_remove, home_dir, claude_dir)

    if backup_successful:
        print("\n  バックアップが完了しました。ファイルの削除を開始します...")
        for path in reversed(files_to_remove):
            try:
                if path.is_file():
                    path.unlink()
                    print(f"    🗑️  削除しました: {path}")
                elif path.is_dir() and not any(p.is_relative_to(path) for p in files_to_remove if p != path):
                    # 他の削除対象ファイルを含まないディレクトリのみを削除
                    if not any(item.is_relative_to(path) for item in files_to_remove if item != path):
                        shutil.rmtree(path)
                        print(f"    🗑️  ディレクトリを削除しました: {path}")

            except Exception as e:
                print_color(f"  ❌ エラー: {path} の削除に失敗しました - {e}", Colors.FAIL)
        print_color("\n  ✅ ファイルのクリーンアップが完了しました。", Colors.OKGREEN)
    else:
        print_color("\n  バックアップに失敗したため、ファイルの削除は行いませんでした。", Colors.FAIL)

def create_backup_strategy(files_to_backup, home_dir, claude_dir):
    """公式バックアップと手動バックアップを組み合わせたハイブリッド戦略を実行"""
    claude_dir_files_exist = any(p == claude_dir or p.is_relative_to(claude_dir) for p in files_to_backup)
    other_files = [p for p in files_to_backup if not (p == claude_dir or p.is_relative_to(claude_dir))]

    official_backup_done = False
    if claude_dir_files_exist and command_exists("SuperClaude"):
        print_color("\n  公式バックアップ機能を使用して ~/.claude をバックアップします...", Colors.OKBLUE)
        result = run_command("SuperClaude backup --create", capture=False)
        if result and result.returncode == 0:
            print_color("  ✅ 公式バックアップが正常に作成されました。", Colors.OKGREEN)
            official_backup_done = True
        else:
            print_color("  ❌ 公式バックアップの作成に失敗しました。手動バックアップにフォールバックします。", Colors.FAIL)

    files_for_manual_backup = []
    if not official_backup_done and claude_dir_files_exist:
         files_for_manual_backup.extend([p for p in files_to_backup if p == claude_dir or p.is_relative_to(claude_dir)])

    files_for_manual_backup.extend(other_files)
    if not files_for_manual_backup: return True

    return create_manual_zip_backup(list(set(files_for_manual_backup)), home_dir)

def create_manual_zip_backup(paths_to_backup, backup_dir):
    """指定されたパスのリストをZIPファイルにバックアップする"""
    print_color("\n  手動でZIPバックアップを作成します...", Colors.OKBLUE)
    backup_base_name = f"{PACKAGE_NAME}_cleanup_backup_{datetime.datetime.now().strftime('%Y%m%d-%H%M%S')}"
    backup_archive_path = backup_dir / backup_base_name
    temp_backup_dir = backup_dir / f"temp_{backup_base_name}"

    try:
        temp_backup_dir.mkdir(exist_ok=True)
        print(f"  バックアップを作成中...")

        for path in paths_to_backup:
            dest_path_segment = None
            try:
                dest_path_segment = path.relative_to(Path.home())
            except ValueError:
                dest_path_segment = Path("__external_paths__") / str(path).lstrip(os.path.sep)

            dest_path = temp_backup_dir / dest_path_segment
            dest_path.parent.mkdir(parents=True, exist_ok=True)

            if path.is_dir():
                shutil.copytree(path, dest_path, dirs_exist_ok=True)
            elif path.is_file():
                shutil.copy2(path, dest_path)

        shutil.make_archive(str(backup_archive_path), 'zip', str(temp_backup_dir))
        print_color(f"  ✅ 手動バックアップが正常に作成されました: {backup_archive_path}.zip", Colors.OKGREEN)
        return True
    except Exception as e:
        print_color(f"  ❌ 手動バックアップの作成中にエラーが発生しました: {e}", Colors.FAIL)
        return False
    finally:
        if temp_backup_dir.exists():
            shutil.rmtree(temp_backup_dir)

def main():
    """スクリプトのメイン処理"""
    print_color("==============================================", Colors.BOLD)
    print_color(f"=== {PACKAGE_NAME.capitalize()} クリーンアップスクリプト（V4対応版） ===", Colors.BOLD)
    print_color("==============================================", Colors.BOLD)
    print("このスクリプトは、システムから全てのSuperClaudeインストールとV3の遺物ファイルを検出し、クリーンアップを試みます。")

    non_interactive = '-y' in sys.argv or '--yes' in sys.argv

    print_color("\n--- CLI版インストールの競合を確認しています ---", Colors.HEADER)
    conflicting_installations = find_conflicting_installations()
    if not conflicting_installations:
        print_color("  競合するCLI版のインストールは見つかりませんでした。", Colors.OKCYAN)
    else:
        print_color(f"  以下の競合するインストールが見つかりました: {', '.join(conflicting_installations)}", Colors.WARNING)
        should_uninstall = non_interactive
        if not non_interactive:
            try:
                answer = input(f"{Colors.WARNING}  これらをアンインストールしますか？ (y/n): {Colors.ENDC}").lower().strip()
                if answer == 'y': should_uninstall = True
            except (KeyboardInterrupt, EOFError):
                print("\n  アンインストールをスキップします。")
        if should_uninstall:
            for manager in conflicting_installations:
                uninstall_package(manager)

    handle_native_plugins_and_legacy_files()
    print_color("\n--- クリーンアップ完了 ---", Colors.HEADER)
    print_color("全ての確認処理が完了しました。", Colors.OKGREEN)
    print("これで、公式プラグインをクリーンインストールする準備が整いました。")

if __name__ == "__main__":
    main()
