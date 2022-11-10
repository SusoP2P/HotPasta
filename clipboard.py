import configparser
import pyclip
from pynput import keyboard
import pyautogui as pya
import time as t


# Clipboard structure

clipboardcfg = configparser.ConfigParser()
clipboard = ""
cblist_count = 0  # Loop counter for 5 Pastas
print("Cblist count index pointing to Pasta " + str(cblist_count + 1))
cblist = ["Pasta 1", "Pasta 2", "Pasta 3", "Pasta 4", "Pasta 5"]

# Create clipboard


def ClipboardCreate():  # Creates the .txt placeholders. Currently not needed as they're implemented in copy_save()
    for i in cblist:
        clipboardcfg[i] = {}
        clipboardcfg[i]["Text"] = ""
        with open("clipboard.txt", "w") as settingsfile:
            clipboardcfg.write(settingsfile)


# list iterators

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

# Copy functions


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
    else:
        pass
    # print(f"Clipboard var is now {clipboard}") # Test: Check clipboard variable
    copy_save()


def copy_save():  # Needs to be changed to send existing pastas to pasta history before overwriting
    global cblist_count
    clipboardcfg[cblist[int(cblist_count)]] = {}
    clipboardcfg[cblist[int(cblist_count)]]["Text"] = f"{clipboard}"
    with open("clipboard.txt", "w") as settingsfile:
        clipboardcfg.write(settingsfile)
    if cblist_count <= 3:
        cblist_count = cblist_count + 1
    elif cblist_count == 4:
        cblist_count = 0
    else:
        cblist_count = 0
        cblist_count = cblist_count + 1
    copy_check()


def copy_check():
    print(f"Check - Text Copied on Pasta {cblist_count}: \n {pyclip.paste()}")
    print("Cblist count index pointing to Pasta " + str(cblist_count + 1))

# Paste functions


def text_paste():  # Pending changes to loop through pastas
    pya.typewrite(pyclip.paste())
    paste_check()


def paste_check():
    print(f"Check - Text Pasted: {pyclip.paste()}")

# Erase functions


def text_erase():
    """
    clipboardcfg[cblist[int(cblist_count) - 1]]["Text"] = ""
    """
    global cblist_count
    print("Erase: cblist_count is " + str({cblist_count}) + " before erase")
    clipboardcfg.read_file(open("clipboard.txt"))
    clipboardcfg.set(cblist[int(cblist_count - 1)], "Text", "")
    with open("clipboard.txt", "w") as settingsfile:
        clipboardcfg.write(settingsfile)
    print(f"Erase: cblist_count is " + str({cblist_count}) + " after erase")
    cblist_count = cblist_count - 1  # if statement missing to fix bug (out of index) when spamming erase
    print(f"cblist_count set to " + str({cblist_count}) + " for next copy")
    erase_check()


def erase_check():
    print('Last Copy deleted!')

# Listeners


def copy_listener():
    print("Check - Copy listened - Executing copy function.")
    text_copy()
    t.sleep(0.5)


def paste_listener():
    print("Check - Paste listened - Executing paste function.")
    paste_check()  # change to text_paste when ready
    t.sleep(0.5)


def erase_listener():
    print("Check - Erase listened - Executing erase function.")
    text_erase()
    t.sleep(0.5)


with keyboard.GlobalHotKeys({
    '<ctrl>+<shift>+c': copy_listener,
    '<ctrl>+<shift>+v': paste_listener,
    '<ctrl>+<shift>+x': erase_listener}) as h:
    h.join()
