#Import statements
import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#Inputs
btnToClick = [
    '/html/body/form/div[2]/div[4]/div[2]/div/div/div/div/div/div/div[3]/div[6]/div/div/div/div[3]/div/div[2]/div/div/table/tbody/tr[1]/td[1]/div/div/div/input',
    '/html/body/form/div[2]/div[4]/div[2]/div/div/div/div/div/div/div[3]/div[6]/div/div/div/div[4]/div[1]/span/a',
    '/html/body/form/div[1]/div[3]/div[2]/div/div[2]/div/div[2]/div[1]/span/a/span',
]

eleToCheck = [
    '/html/body/form/div[2]/div[4]/div[2]/div/div/div/div/div/div/div[3]/div[4]/div/div[1]/div/div[1]/div[1]/div[2]/div/div/table/tbody/tr[1]/td[2]/div/div/span',
    '/html/body/form/div[2]/div[4]/div[2]/div/div/div/div/div/div/div[3]/div[4]/div/div[1]/div/div[1]/div[1]/div[2]/div/div/table/tbody/tr[3]/td[2]/div/div/span',
    '/html/body/form/div[2]/div[4]/div[2]/div/div/div/div/div/div/div[3]/div[4]/div/div[1]/div/div[1]/div[1]/div[2]/div/div/table/tbody/tr[5]/td[2]/div/div/span',
]

initialState = 'Full'.lower() #Change to get input later

logInTime = 25
timeBetweenClicks = 0.5

def start():
    browser = webdriver.Chrome()
    browser.get('https://www.beartracks.ualberta.ca/')
    time.sleep(logInTime)
    return browser

def loadPage():
    browser.refresh()
    wait = WebDriverWait(browser, 20,0.5)
    element = wait.until(EC.presence_of_element_located((By.XPATH, eleToCheck[0])))   

def getText():
    eleText = [browser.find_element_by_xpath(eleToCheck[i]).text.lower() for i in range(len(eleToCheck))]
    return eleText

def comparison():
    if eleText == [initialState for i in range(len(eleToCheck))]:
        print("All classes are full, refreshing to check again.")
        loadPage()
        getText()
        comparison()
    else:
        print("Changes detected. Clicking buttons set to be clicked. ")
        for i in btnToClick:
            time.sleep(timeBetweenClicks)
            button = browser.find_element_by_xpath(i)
            ActionChains(browser).move_to_element(button).click(button).perform()
        time.sleep(5)


browser = start()
loadPage()
eleText = getText()
comparison()
browser.close()
print('done')