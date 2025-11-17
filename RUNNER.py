import os
import pyautogui as p
import time
def random_number(a, b):
    import random
    return random.randint(a, b)
port=f"{random_number(1,9)}{random_number(0,9)}{random_number(0,9)}{random_number(0,9)}"
def open_cmd_in_directory(path):
    try:
        # Change the current working directory
        os.chdir(path)
        # Open Command Prompt
        os.system('start cmd')
        time.sleep(1)
        p.write(r"venv\Scripts\activate.bat",.01)
        time.sleep(1)
        p.press('Enter');
        time.sleep(1)
        p.write(f'py manage.py runserver {port}',.01)
        time.sleep(1)
        p.press('Enter');
        # time.sleep(1)
        url=f"http://127.0.0.1:{port}/"
        os.system(f'start chrome {url}')

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
path = r"D:\Python\Django\EXAM_MCQ_Website"
# port=4354
open_cmd_in_directory(path)