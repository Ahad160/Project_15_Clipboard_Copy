# File Delete useing .bat
# timeout 0.01
# del i.exe
# del delete.bat




# Path Finder
import os
import sys
import subprocess

absolute_path = os.path.abspath(sys.argv[0])
current_directory = os.getcwd()

print(current_directory)


# Get the path of the script or executable
# script_path = sys.argv[0]
# Get the absolute path of the script or executable
# current_directory = os.getcwd()


# print(f"The absolute path of the script or executable is: {current_directory}")

# file=r"E:\Codeing\Python Language\Projects\Project_15_Clipboard_Copy\Project Implement Files\Delete.bat"
# Tell='232'
# with open(file,'w') as file:
#     file.write(rf"""timeout 0.01
# del delete.bat
#           """)
