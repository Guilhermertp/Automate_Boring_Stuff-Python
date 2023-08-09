
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
browser.get('https://google.com/')

#stores a web element object in the variable elem that will be used to automate the click
elem = browser.find_element_by_css_selector('#L2AGLb > div')

#simulates the click method in the element to accept the google privacy setting
elem.click()

#assign the a variable the selector for the search in google
searchElem = browser.find_element_by_css_selector('body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input')

#pass any string into the search bar
searchElem.send_keys('nasa')

#Selenium finds the html related to the text field (string passed above (nasa))
#i don't need to click to get the result of the search
searchElem.submit()

#store text element
elem = browser.find_element_by_css_selector('#rso > div:nth-child(1) > div > div > div > div > div > div > div.IsZvec > div')

#display in the console the text in the text element
print(elem.text)
