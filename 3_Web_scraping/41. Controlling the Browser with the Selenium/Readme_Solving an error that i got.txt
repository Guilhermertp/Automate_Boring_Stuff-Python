The easiest way is to use webdriver-manager1 which is a library “to automatically manage drivers for different browsers”.

********1.1****************
Install with the command: pip install webdriver_manager

********1.2 Use************
In your code use the right manager for Selenium’s webdriver
and then Choose the right browser:

from selenium import webdriver # this code have to come first if we run each line of code in the terminal!!!


****Chrome****
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())

***Firefox***
from webdriver_manager.firefox import GeckoDriverManager
browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())

***Internet Explorer***
from webdriver_manager.microsoft import IEDriverManager

browser = webdriver.Ie(IEDriverManager().install())

***Edge***
from webdriver_manager.microsoft import EdgeChromiumDriverManager

browser = webdriver.Edge(EdgeChromiumDriverManager().install())




Reference: https://simpleit.rocks/python/selenium-webdriver-exception-executable-in-path-error/

Another source of info for selenium: https://www.tutorialspoint.com/how-to-invoke-the-chrome-browser-in-selenium-with-python