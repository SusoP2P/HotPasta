# Module reference file. All dependencies with module-specific files separate.
#
#
#
# Reserved for comments and fancy space
import settings


def tutorial():
    print("Tutorial prompted")


def onboarding():
    print("Onboarding promtped")


def menu_show():
    print("Menu shown")


def menu_hide():
    print("Menu not shown. App started in background")


def overlay_show():
    print("Overlay shown")


def set_internal_settings():
    print("Internal Settings set")


def DefaultSettings():
    settings.CreateDefaultSettings()


def security_check():
    print("Security Check passed!")


def generic_error():
    print("Generic Error")
