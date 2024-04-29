import os
import sys
import ctypes
import winreg

def add_to_startup():
    # Get the path to the current script
    script_path = os.path.abspath(sys.argv[0])

    # Create the registry key for the startup entry
    key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
    key_name = "MyPythonScript"
    
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE) as key:
            winreg.SetValueEx(key, key_name, 0, winreg.REG_SZ, script_path)
        print(f"Added to startup: {script_path}")
    except Exception as e:
        print(f"Error adding to startup: {e}")

if __name__ == "__main__":
    # Check if running with administrative privileges
    if not ctypes.windll.shell32.IsUserAnAdmin():
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        sys.exit()

    # Add the script to startup
    add_to_startup()
