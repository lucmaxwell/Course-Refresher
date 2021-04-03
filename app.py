import time
from selenium import webdriver
import binascii
from selenium.webdriver.common.action_chains import ActionChains

logInTime = 30
refreshTime = 5
timeBetweenFirstTwoScreenshots = 2 #Not recommended to go lower than 2 since page will not be loaded before screenshots are taken
timeBetweenClicks = 0.4

btnToClick = [
    '/html/body/form/div[2]/div[4]/div[2]/div/div/div/div/div/div/div[3]/div[6]/div/div/div/div[3]/div/div[2]/div/div/table/tbody/tr[1]/td[1]/div/div/div/input',
    '/html/body/form/div[2]/div[4]/div[2]/div/div/div/div/div/div/div[3]/div[6]/div/div/div/div[3]/div/div[2]/div/div/table/tbody/tr[3]/td[1]/div/div/div/input',
    '/html/body/form/div[2]/div[4]/div[2]/div/div/div/div/div/div/div[3]/div[6]/div/div/div/div[4]/div[1]/span/a',
    '/html/body/form/div[1]/div[3]/div[2]/div/div[2]/div/div[2]/div[1]/span/a/span',
    ]

def start():
    global iterable
    global photos
    global counter
    counter = 0
    iterable = True
    photos = ['0', '0']
    browser.refresh()
    time.sleep(timeBetweenFirstTwoScreenshots)
    browser.save_screenshot(f"screenshot{int(iterable)}.png")
    with open(f"screenshot{int(iterable)}.png", 'rb') as image:
        hexa = binascii.hexlify(image.read())
    photos[int(iterable)] = hexa
    iterable = not iterable


browser = webdriver.Chrome()
browser.get('https://www.beartracks.ualberta.ca/')

time.sleep(logInTime)

start()

while True:
    try:
        browser.refresh()
        time.sleep(timeBetweenFirstTwoScreenshots)
        browser.save_screenshot(f"screenshot{int(iterable)}.png")
        with open(f"screenshot{int(iterable)}.png", 'rb') as image:
            hexa = binascii.hexlify(image.read())
        photos[int(iterable)] = hexa
        iterable = not iterable
        counter += 1

        if photos[0] == photos[1]: 
            print(f"No changes detected. Searching again for changes. ({counter})")
            time.sleep(refreshTime)
            raise Exception("No change")

        else:
            print("Changes detected. Clicking buttons set to be clicked. ")
            for i in btnToClick:
                time.sleep(timeBetweenClicks)
                button = browser.find_element_by_xpath(i)
                ActionChains(browser).move_to_element(button).click(button).perform()
            time.sleep(10)
            message = input("Type 'exit' and then press enter to exit the program. Press any other key(s) and press enter to continue running the program. \n> ")
            if message.strip() == 'exit' or message.strip() == 'Exit':
                break
            else:
                start()
    except:
        pass


browser.close()


"""
Things to fix on next iteration: 
- Create GUI
- Make page load before screenshots are taken automatically
- Allow it to run in the background
- 
"""