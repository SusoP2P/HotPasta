#
#
#
#
#Reserved for comments and fancy space
import configparser
settings = configparser.ConfigParser()
settings['DEFAULT'] = {'Setting1': '2',
                     'Setting2': 'True',
                     'Setting3': '0.1'}
settings['AUDIO'] = {}
settings['AUDIO']['Setting21'] = 'hg'
with open('settings.ini', 'w') as settingsfile:
  settings.write(settingsfile)

# Savebutton():
# with open('settings.ini', 'r') as settingsfile:
#  settings.write(settingsfile)