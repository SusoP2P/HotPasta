import configparser
import pyclip
from settings import config
from pynput import keyboard
import pyautogui as pya
import time as t

from win32gui import GetWindowText, GetForegroundWindow
import win32ui

print(GetWindowText(GetForegroundWindow()))
wnd = GetForegroundWindow()
print(GetWindowText(wnd))

# Default values

pasta_loop = 0  # needed for innit_loop()
clipboard = ""
stored_cb = f"{pyclip.paste()}"
print(f"Windows clipboard is: \n {stored_cb}")
cblist = ["Pasta 1", "Pasta 2", "Pasta 3", "Pasta 4", "Pasta 5"]
clipboardcfg = configparser.ConfigParser()


# Initialization

def CheckClipboard():  # Creates the .txt placeholders or initializes the settings
    if not clipboardcfg.read("clipboard.txt"):
        for i in cblist:
            clipboardcfg[i] = {"Text": ""}
            with open("clipboard.txt", "w") as settingsfile:
                clipboardcfg.write(settingsfile)
    else:
        innit_loop()


def innit_loop():
    global pasta_loop
    global clipboard

    config.read_file(open("settings.ini"))
    pasta_loop = int(config["STARTUP"]["cblist_count"])  # Retrieve / save index position.
    print(f"Start check: cblist_count is {pasta_loop} pointing to Pasta {str(pasta_loop + 1)}")

    clipboardcfg.read_file(open("clipboard.txt"))
    clipboard = clipboardcfg[cblist[pasta_loop]]["Text"]
    print(f"Current Pasta is: \n {clipboard}")


CheckClipboard()

# list iterators (for potential changes to the file creation)

"""
for item in cblist:
    cblist[+=1]
    print(cblist)

for index, item in enumerate(cblist, start=1):
    cblist_count = index + 1
    print(index, item, cblist_count)
for item in cblist:

    print(range(len(cblist)))
"""


# Loop control

def check_loop():
    global pasta_loop
    if pasta_loop in [5, -5]:
        print(f"Loop targeting index {pasta_loop}. Setting to 0.")
        pasta_loop = 0
    else:
        print(f"Loop targeting index {pasta_loop}. No further action needed.")


def loop_forward():
    global pasta_loop
    check_loop()
    pasta_loop = pasta_loop + 1
    check_loop()


def loop_backward():
    global pasta_loop
    check_loop()
    pasta_loop = pasta_loop - 1
    check_loop()


# Copy functions
def copy_check():
    print(f"Check - Text Copied on Pasta {pasta_loop}: \n {pyclip.paste()}")
    print(f"Cblist count index pointing to Pasta {str(pasta_loop + 1)}")


def copy_save():  # Needs to be changed to send existing pastas to pasta history before overwriting

    global pasta_loop

    clipboardcfg[cblist[int(pasta_loop)]] = {"Text": f"{clipboard}"}
    with open("clipboard.txt", "w") as settingsfile:
        clipboardcfg.write(settingsfile)

    loop_forward()

    copy_check()


def text_copy():  # Needs to be changed in order to copy the user selected text instead of using CTRL + C
    global clipboard

    pya.keyUp('c')
    pya.keyUp('shift')
    pya.keyUp('ctrl')
    t.sleep(0.1)

    pya.keyDown('ctrl')
    pya.keyDown('c')
    t.sleep(0.1)

    pya.keyUp('c')
    pya.keyUp('ctrl')
    pya.keyUp('shift')

    if str(pyclip.paste()):
        clipboard = pyclip.paste()
    # print(f"Clipboard var is now {clipboard}")  # Test: Check clipboard variable

    copy_save()


# Paste functions


def paste_check():
    global clipboard
    print(f"Check - Text Pasted: {clipboard}")


def text_paste():  # Pending changes to loop through pastas. Needs GUI for paste logic into it.
    global clipboard
    global stored_cb

    pyclip.clear()

    pya.keyUp('v')
    pya.keyUp('shift')
    pya.keyUp('ctrl')

    # print(f"Clipboard var is now {clipboard}. Attempting to paste")  # Test: Check clipboard variable
    pya.typewrite(f"{clipboard}")
    # print(f"Clipboard var is now {clipboard}")  # Test: Check clipboard variable

    pyclip.copy(stored_cb)

    pya.keyDown('ctrl')
    pya.keyDown('shift')

    paste_check()


# Currently not in use. This is for future testing


""" if clipboard != "":
        pya.typewrite(pyclip.paste())
        paste_check()
    else:
        pass"""


# Erase functions

def erase_check():
    print('Last Copy deleted!')


def text_erase():
    global pasta_loop
    print(f"Erase: cblist_count is {pasta_loop}  before erase")

    clipboardcfg.read_file(open("clipboard.txt"))
    clipboardcfg.set(cblist[int(pasta_loop - 1)], "Text", "")
    with open("clipboard.txt", "w") as settingsfile:
        clipboardcfg.write(settingsfile)

    print(f"Erase: cblist_count is {pasta_loop} after erase")
    loop_backward()
    print(f"cblist_count set to {pasta_loop} for next copy")

    erase_check()


# Listeners

def copy_listener():
    print("Check - Copy listened - Executing copy function.")
    text_copy()
    t.sleep(0.1)


def paste_listener():
    print("Check - Paste listened - Executing paste function.")
    text_paste()
    t.sleep(0.1)


def erase_listener():
    print("Check - Erase listened - Executing erase function.")
    text_erase()
    t.sleep(0.1)


with keyboard.GlobalHotKeys({
    '<ctrl>+<shift>+c': copy_listener,
    '<ctrl>+<shift>+v': paste_listener,
    '<ctrl>+<shift>+x': erase_listener})\
        as h:
    h.join()
    t.sleep(0.1)
