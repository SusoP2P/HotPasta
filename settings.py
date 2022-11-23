# Internal and Default settings
#
#
#
# Reserved for comments and fancy space
import configparser
#  import clipboard as cb  # Circular import
from modules import *

config = configparser.ConfigParser()  # variable for configparser

# Initialization functions


def check_first_boot():  # Check boot status for Onboarding and potentially other stuff
    config.read("settings.ini")

    if not config.read("settings.ini"):
        DefaultSettings()
        # cb.CheckClipboard()  # This might not be needed. CAREFUL: Potential cirular import
        check_first_boot()
    elif config["DEFAULT"].getboolean("firstboot"):
        config["DEFAULT"]["firstboot"] = "False"
        with open('settings.ini', 'w') as configfile:
            config.write(configfile)
        onboarding()
    elif not config["DEFAULT"].getboolean("firstboot"):
        if config["STARTUP"].getboolean("launchminimized"):
            print("App launched minimized")
        if not config["STARTUP"].getboolean("launchminimized"):
            ShowMenu()
    else:
        generic_error()


def ShowMenu():  # Decide whether to show the menu or not
    config.read("settings.ini")
    if config["DEFAULT"].getboolean("showmenu"):
        menu_show()
    elif not config["DEFAULT"].getboolean("showmenu"):
        menu_hide()
    else:
        generic_error()

# These are the internal settings that the program needs to run properly
# They are non-editable by default and only advanced users who understand the code should change them
# Reserved for comments and fancy space


# These are the default settings that users can edit freely


def CreateDefaultSettings():  # Creates the default settings
    config["DEFAULT"] = {"firstboot": "True",
                         "showmenu": "True",
                         "cblist_count": "0",
                         "Setting3": "0.1"}
    config["STARTUP"] = {"launchatstartup": "True", "launchminimized": "True"}
    with open("settings.ini", "w") as settingsfile:
        config.write(settingsfile)
    print("Default Settings created")


# GUI Components

def SaveButton():  # Save button for GUI
    with open("settings.ini", "r") as settingsfile:
        config.write(settingsfile)
