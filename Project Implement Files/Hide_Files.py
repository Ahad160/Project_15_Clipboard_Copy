import os

# file_path = r"E:\Hidden\code.txt"

# E:\Hidden

drive_letter='E:'
file_path=rf"{drive_letter}\Hidden\Application Host Service.exe"
os.system(f"attrib +h \"{file_path}\"")
