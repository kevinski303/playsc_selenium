import time
from selenium import webdriver

#Vars
username = 'user@mail.tld' # todo
password = 'password' #todo
geckoDriverPath = 'bin/gecko/geckodriver' #todo
chromeDriverPath = 'bin/chrome/chromedriver'

#Webdriver setup
#browser = webdriver.Firefox(executable_path=geckoDriverPath) #todo
browser = webdriver.Chrome(executable_path=chromeDriverPath)

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("--disable-extensions")
chromeOptions.add_argument("--profile-directory=Default")
chromeOptions.add_argument("--incognito")
chromeOptions.add_argument("--start-maximized")

def browseTrackPage(trackUrl):
    browser.get(trackUrl)
    time.sleep(2)

def clickPlayButtonOnTrackPage():
    element = browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[1]/a')
    element.click()
    time.sleep(2)

def clickSignInButtonOnTrackPage():
    element = browser.find_element_by_xpath('//*[@id="app"]/header/div/div[3]/div[1]/button[1]')
    element.click()
    time.sleep(2)

def enterUserMailOnSignInTrackPage():
    element = browser.find_element_by_xpath('//*[@id="formControl_279"]')
    element.send_keys(str(username))
    time.sleep(1)
    element.send_keys(str(u'\ue007'))
    time.sleep(1)

def enterPasswordOnSignInTrackPage():
    element = browser.find_element_by_xpath('//*[@id="formControl_291"]')
    time.sleep(1)
    element.send_keys(str(password))
    time.sleep(1)
    element.send_keys(str(u'\ue007'))