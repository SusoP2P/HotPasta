# Internal and Default settings
#
#
#
# Reserved for comments and fancy space
import configparser
import modules

# Initialization functions


def check_first_boot():  # This checks boot status for Onboarding and potentially other stuff
    config.read("settings.ini")
    if config.read("settings.ini") == []:
        modules.DefaultSettings()
        check_first_boot()
    elif config["DEFAULT"].getboolean("firstboot") == True:
        config["DEFAULT"]["firstboot"] = "False"
        with open('settings.ini', 'w') as configfile:
            config.write(configfile)
        modules.onboarding()
    elif config["DEFAULT"].getboolean("firstboot") == False:
        ShowMenu()
    else:
        modules.GenericError()


def ShowMenu():
    config.read("settings.ini")
    if config["DEFAULT"].getboolean("showmenu") == True:
        modules.menu_show()
    elif config["DEFAULT"].getboolean("showmenu") == False:
        modules.menu_hide()
    else:
        modules.GenericError()

# These are the internal settings that the program needs to run properly
# They are non-editable by default and only advanced users who understand the code should change them
# Reserved for comments and fancy space

# These are the default settings that users can edit freely


config = configparser.ConfigParser()


def CreateDefaultSettings():  # Creates the default settings
    config["DEFAULT"] = {"firstboot": "True",
                     "showmenu": "True",
                     "Setting3": "0.1"}
    config["AUDIO"] = {}
    config["AUDIO"]["Setting21"] = "hg"
    with open("settings.ini", "w") as settingsfile:
        config.write(settingsfile)
    print("Default Settings created")


# GUI Components

def SaveButton():  # Save button for GUI
    with open("settings.ini", "r") as settingsfile:
        config.write(settingsfile)



