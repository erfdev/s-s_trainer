'''
    ss_connect.py
    -------------
    Script to open up Firefox/Chrome browser and open Swords and Souls web page.

    Will need geckodriver for Firefox, or chromedriver for Chrome
    [https://github.com/mozilla/geckodriver/releases]
    [https://github.com/SeleniumHQ/selenium/wiki/ChromeDriver]

'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

profile = webdriver.FirefoxProfile()
profile.set_preference('plugin.state.flash', 2)
driver = webdriver.Firefox(profile)

game_url = "https://www.kongregate.com/games/SoulGame/swords-and-souls"

driver.get(game_url)

#driver.close()


#FIXME : Enable Flash Plugin for Chrome ...

#options = webdriver.ChromeOptions()
#
#
#prefs = {
#    "profile.default_content_setting_values.plugins": 1,
#    "profile.content_settings.plugin_whitelist.adobe-flash-player": 1,
#    "profile.content_settings.exceptions.plugins.*,*.per_resource.adobe-flash-player": 1,
#    "PluginsAllowedForUrls": "https://www.kongregate.com/games/SoulGame/swords-and-souls"
#}
#options.add_experimental_option("prefs",prefs)
#
#driver = webdriver.Chrome(chrome_options=options)


