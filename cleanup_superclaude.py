
import datetime
import os
import platform
import shutil
import subprocess
import sys

# --- 設定 ---
PACKAGE_NAME = "superclaude"
COMMAND_PACKAGES = {
    'pip': PACKAGE_NAME,
    'pipx': PACKAGE_NAME,
    'uv': PACKAGE_NAME,
    'npm': PACKAGE_NAME
}

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
        if capture:
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                encoding='utf-8',
                check=False
            )
        else:
            result = subprocess.run(
                command,
                shell=True,
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

def check_installation(manager, package):
    """指定されたパッケージマネージャーでパッケージがインストールされているか確認する"""
    if not command_exists(manager):
        return False

    check_command = {
        'pip': f"pip show {package}",
        'pipx': "pipx list",
        'uv': f"uv pip show {package}",
        'npm': f"npm list -g {package}"
    }.get(manager)

    result = run_command(check_command)

    if result and result.returncode == 0 and result.stdout:
        if manager == 'pipx':
            return package in result.stdout
        return True
    return False

def find_conflicting_installations(package):
    """競合する可能性のある全てのインストールを検知し、リストを返す"""
    conflicts = []
    for manager in COMMAND_PACKAGES.keys():
        if check_installation(manager, package):
            conflicts.append(manager)
    return conflicts

# --- アンインストール処理 ---

def uninstall_package(manager, package):
    """指定されたパッケージマネージャーからパッケージをアンインストールする"""
    print_color(f"\n--- {manager.upper()} から '{package}' をアンインストールします ---", Colors.HEADER)

    uninstall_command = {
        'pip': f"pip uninstall -y {package}",
        'pipx': f"pipx uninstall {package}",
        'uv': f"uv pip uninstall -y {package}",
        'npm': f"npm uninstall -g {package}"
    }.get(manager)

    run_command(uninstall_command, capture=False)

    print(f"\n  アンインストールが成功したか再確認しています...")
    if not check_installation(manager, package):
        print_color(f"  ✅ {manager} から '{package}' を正常にアンインストールしました。", Colors.OKGREEN)
    else:
        print_color(f"  ❌ {manager} から '{package}' のアンインストールに失敗した可能性があります。", Colors.FAIL)
        print_color(f"     手動で '{uninstall_command}' を実行してみてください。", Colors.FAIL)

def handle_native_plugins():
    """ネイティブプラグインを検出し、バックアップを作成した上で手動削除を案内する"""
    print_color("\n--- ネイティブプラグインの確認 ---", Colors.HEADER)

    system = platform.system()
    home_dir = os.path.expanduser("~")
    paths_to_check = []
    capitalized_package_name = PACKAGE_NAME.capitalize()

    if system == "Darwin":
        paths_to_check.extend([
            os.path.join(home_dir, f"Library/Application Support/{capitalized_package_name}"),
            f"/Library/Application Support/{capitalized_package_name}"
        ])
    elif system == "Windows":
        appdata = os.getenv('APPDATA')
        local_appdata = os.getenv('LOCALAPPDATA')
        program_files = os.getenv('ProgramFiles')
        if appdata: paths_to_check.append(os.path.join(appdata, capitalized_package_name))
        if local_appdata: paths_to_check.append(os.path.join(local_appdata, capitalized_package_name))
        if program_files: paths_to_check.append(os.path.join(program_files, capitalized_package_name))
    elif system == "Linux":
        paths_to_check.extend([
            os.path.join(home_dir, f".config/{PACKAGE_NAME}"),
            os.path.join(home_dir, f".local/share/{PACKAGE_NAME}"),
            f"/usr/share/{PACKAGE_NAME}",
            f"/opt/{PACKAGE_NAME}"
        ])
    else:
        print_color(f"\n不明なOS ({system}) のため、ネイティブプラグインは確認できません。", Colors.WARNING)
        return

    existing_paths = [p for p in paths_to_check if os.path.exists(p)]

    if not existing_paths:
        print_color("  関連するネイティブプラグインのディレクトリは見つかりませんでした。", Colors.OKCYAN)
        return

    print_color("  以下の場所にネイティブプラグインのディレクトリが見つかりました：", Colors.WARNING)
    for path in existing_paths:
        print(f"    -> {path}")

    non_interactive = '-y' in sys.argv or '--yes' in sys.argv
    do_backup = False
    if non_interactive:
        do_backup = True
    else:
        try:
            answer = input(f"\n{Colors.WARNING}  これらのディレクトリを削除する前にバックアップを作成しますか？ (y/n): {Colors.ENDC}").lower().strip()
            if answer == 'y':
                do_backup = True
        except (KeyboardInterrupt, EOFError):
            print("\n  バックアップをスキップします。")

    if do_backup:
        # 公式のバックアップコマンドを優先
        if command_exists("SuperClaude"):
            print("  公式バックアップ機能を使用してバックアップを作成します...")
            backup_command = "SuperClaude backup --create"
            result = run_command(backup_command, capture=False)
            if result and result.returncode == 0:
                print_color("  ✅ 公式バックアップが正常に作成されました。", Colors.OKGREEN)
            else:
                print_color("  ❌ 公式バックアップの作成に失敗しました。", Colors.FAIL)
        else:
            # フォールバックとしてZIPバックアップを作成
            print_color("  SuperClaudeコマンドが見つかりません。手動でZIPバックアップを作成します。", Colors.WARNING)
            backup_base_name = f"{PACKAGE_NAME}_backup_{datetime.datetime.now().strftime('%Y%m%d-%H%M%S')}"
            backup_archive_path = os.path.join(home_dir, backup_base_name)
            temp_backup_dir = os.path.join(home_dir, f"temp_{backup_base_name}")

            try:
                os.makedirs(temp_backup_dir, exist_ok=True)
                print(f"  バックアップを作成中...")
                for path in existing_paths:
                    dest_path = os.path.join(temp_backup_dir, os.path.basename(os.path.normpath(path)))
                    if os.path.isdir(path):
                        shutil.copytree(path, dest_path)
                    elif os.path.isfile(path):
                        shutil.copy2(path, dest_path)

                shutil.make_archive(backup_archive_path, 'zip', temp_backup_dir)
                print_color(f"  ✅ 手動バックアップが正常に作成されました: {backup_archive_path}.zip", Colors.OKGREEN)
            except Exception as e:
                print_color(f"  ❌ 手動バックアップの作成中にエラーが発生しました: {e}", Colors.FAIL)
            finally:
                if os.path.exists(temp_backup_dir):
                    shutil.rmtree(temp_backup_dir)

    print_color("\n  ネイティブプラグインは自動で削除できません。", Colors.WARNING)
    print("  バックアップを取得した後、以下のディレクトリを手動で削除してください：")
    for path in existing_paths:
        print_color(f"    -> {path}", Colors.WARNING)


def main():
    """スクリプトのメイン処理"""
    print_color("==============================================", Colors.BOLD)
    print_color(f"=== {PACKAGE_NAME.capitalize()} クリーンアップスクリプト ===", Colors.BOLD)
    print_color("==============================================", Colors.BOLD)
    print("このスクリプトは、システムから全てのSuperClaudeインストールを検出し、削除を試みます。")

    non_interactive = '-y' in sys.argv or '--yes' in sys.argv

    # --- CLI版の競合を確認 ---
    print_color("\n--- CLI版インストールの競合を確認しています ---", Colors.HEADER)
    conflicting_installations = find_conflicting_installations(PACKAGE_NAME)

    if not conflicting_installations:
        print_color("  競合するCLI版のインストールは見つかりませんでした。", Colors.OKCYAN)
    else:
        print_color(f"  以下の競合するインストールが見つかりました: {', '.join(conflicting_installations)}", Colors.WARNING)

        should_uninstall = False
        if non_interactive:
            should_uninstall = True
        else:
            try:
                answer = input(f"{Colors.WARNING}  これらをアンインストールしますか？ (y/n): {Colors.ENDC}").lower().strip()
                if answer == 'y':
                    should_uninstall = True
            except (KeyboardInterrupt, EOFError):
                print("\n  アンインストールをスキップします。")

        if should_uninstall:
            for manager in conflicting_installations:
                uninstall_package(manager, PACKAGE_NAME)

    # --- ネイティブプラグインの確認 ---
    handle_native_plugins()

    print_color("\n--- クリーンアップ完了 ---", Colors.HEADER)
    print_color("全ての確認処理が完了しました。", Colors.OKGREEN)
    print("ネイティブプラグインに関する指示を確認し、必要に応じて手動で削除してください。")
    print("これで、公式プラグインをクリーンインストールする準備が整いました。")

if __name__ == "__main__":
    main()
