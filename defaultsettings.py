# These are the default settings that users can edit freely
#
#
#
#Reserved for comments and fancy space
import configparser
import modules


config = configparser.ConfigParser()


def CreateDefaultSettings():
    config["DEFAULT"] = {"firstboot": "True",
                     "Setting2": "True",
                     "Setting3": "0.1"}
    config["AUDIO"] = {}
    config["AUDIO"]["Setting21"] = "hg"
    with open("settings.ini", "w") as settingsfile:
        config.write(settingsfile)
    print("Default Settings created")


def SaveButton():
    with open("settings.ini", "r") as settingsfile:
        config.write(settingsfile)

def check_first_boot():
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
        modules.menu_show()
    else:
        modules.GenericError()

"""print(config.read("settings.ini"))"""