import pyperclip
import time


HISTORY_FILE = r"E:\clipboard_history.txt"

def update_history(text):
    try:
        with open(HISTORY_FILE, "r") as file:
            history = file.readlines()
    except FileNotFoundError:
        history = []

    # # Add new text to history
    if text and text not in history:
            # Save history to file 
        with open(HISTORY_FILE, 'a', encoding='utf-8') as file:
            file.write(f'\n{text}')    
            

def check_clipboard():
    try:
        clipboard_text = pyperclip.paste()
        update_history(clipboard_text)
    except Exception as e:
        # Handle exceptions (e.g., clipboard contains non-text data)
        pass


while True:
    check_clipboard()
    time.sleep(5)  # Check clipboard every 1 second
