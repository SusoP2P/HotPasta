"""
# Test from https://nitratine.net/blog/post/how-to-make-hotkeys-in-python/#installing-pynput

import pyclip
import clipboard as cb
from pynput import keyboard
import pyautogui as pya
import time as t


# Text Functions

print(cb.cblist_count)


def text_copy():
    pya.keyUp('ctrl')
    pya.keyUp('shift')
    pya.keyUp('c')
    t.sleep(0.1)
    pya.keyDown('ctrl')
    pya.keyDown('c')
    t.sleep(0.1)
    pya.keyUp('c')
    pya.keyUp('shift')
    pya.keyUp('ctrl')
    if str(pyclip.paste()):
        cb.clipboard = pyclip.paste()
    else:
        pass
    # print(f"Clipboard var is now {cb.clipboard}") # Check clipboard variable
    cb.copy_save()
    copy_check()


def copy_check():
    print(f"Check - Text Copied: {pyclip.paste()}")


def text_paste():
    pya.typewrite(pyclip.paste())
    paste_check()


def paste_check():
    print(f"Check - Text Pasted: {pyclip.paste()}")


def text_erase():
    cb.clipboardcfg.read_file(open("clipboard.txt"))
    cb.clipboardcfg.set(cb.cblist[int(cb.cblist_count)], "Text", "")
    with open("clipboard.txt", "w") as settingsfile:
        cb.clipboardcfg.write(settingsfile)
    erase_check()



clipboardcfg.read_file(open("clipboard.txt"))
clipboardcfg.set("Pasta 5", "Text", "")
with open("clipboard.txt", "w") as settingsfile:
    clipboardcfg.write(settingsfile)



def erase_check():
    print('Last Copy deleted!')


# Text Listeners


def copy_listener():
    print("Check - Copy listened - Executing copy function.")
    text_copy()
    t.sleep(0.5)


def paste_listener():
    print("Check - Paste listened - Executing paste function.")
    paste_check()  # change to text_paste when ready


def erase_listener():
    print("Check - Erase listened - Executing erase function.")
    erase_check()  # change to text_erase when ready




with keyboard.GlobalHotKeys({
cc    '<ctrl>+<shift>+x': erase_listener}) as h:
    h.join()


pyclip.copy("hello clipboard") # copy data to the clipboard
ccb_text = pyclip.paste(text=True)  # paste as text
print(cb_text)  # 'hello clipboard'

pyclip.clear() # clears the clipboard contents
assert not pyclip.paste()
"""