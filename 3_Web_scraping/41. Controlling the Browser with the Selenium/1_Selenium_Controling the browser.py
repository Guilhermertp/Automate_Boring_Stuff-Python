#if it is not installed install the selenium module going to the command line and typing:  pip install selenium
from selenium import webdriver

#opens a new window on google chrome
#this code works but gives an erro and not allows to specify an url afterwards
#browser = webdriver.Chrome(executable_path="C:\Program Files\Google\Chrome\Application\chrome.exe")

#the solution is to install the chromedrive or other depending on the browser of choice
# solution in the Readme file

from webdriver_manager.chrome import ChromeDriverManager

#to install the chromedrive
browser = webdriver.Chrome(ChromeDriverManager().install())

#open a specific url witht he selenium module
browser.get('https://automatetheboringstuff.com/')

#stores a web element object in the variable elem that will be used to automate the click
elem = browser.find_element_by_css_selector('body > div > main > div > ul:nth-child(19) > li:nth-child(13) > a')

#simulates the click method in the element
elem.click()

#return elements objects from the paragraphs of the page choosen
elems = browser.find_elements_by_css_selector('p')
print(len(elems))#displays the lenght of the objects

