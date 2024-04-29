import time
import win32clipboard


HISTORY_FILE = "clipboard_history.txt"
MAX_HISTORY_SIZE = 100  # Adjust this value based on your preference

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

while True:
    check_clipboard()
    time.sleep(5)  # Check clipboard every 1 second
