from __future__ import unicode_literals
import random
import time
import keyboard
import string
import pyautogui
import secrets
from faker import Faker
from pynput.keyboard import Key, Controller
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Chrome
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

genam = 30
captchakeygen = "".join(random.choice(string.ascii_letters) for i in range(genam))
print("Your captcha key is: " + captchakeygen)

###SETTING LINKS###
mailsite = "https://temp-mail.org/en/"
twitchsite = "https://www.twitch.tv/"



#SETTING DETAILS#
usertofollow = input("\n\tPlease enter targets username \n\tPress Enter For None \n\t--> ")
amount = int(input("How many to create and follow: "))
chromepath = "C:\chromedriver\chromedriver.exe"

#SETTING CHROME OPTIONS#
chrome_options = Options()
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("--incognito")
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('disable-infobars')
driver = webdriver.Chrome(chromepath, options=chrome_options)

for i in range(0, amount):
    ###COPYING EMAIL###
    driver.get(mailsite)
    print(driver.title)
    time.sleep(10)

    #Start copying email
    element = driver.find_element_by_id("mail")
    element.click()
    time.sleep(1)
    keyboard.press_and_release("ctrl+c")

    print("Coppied email")
    time.sleep(2)

    ###STOPPING CHROME CONTROL NOTI###
    pyautogui.moveTo(1898, 92)
    pyautogui.click()
    time.sleep(2)

    ###NEW TAB###
    driver.execute_script("window.open('about:blank', 'tab2');")
    driver.switch_to.window("tab2")

    #LOADING TWITCH#
    driver.get(twitchsite)
    time.sleep(5)
    pyautogui.moveTo(1834, 216)
    pyautogui.click()
    time.sleep(5)


    ###CREATING USERNAME###
    upper_case = 1
    name_upper_chars = string.ascii_uppercase
    upper_name = ''.join(random.choice(name_upper_chars) for y in range(upper_case))
    name_size = random.randint(8, 16)
    name_chars = string.ascii_lowercase
    name = ''.join(random.choice(name_chars) for x in range(name_size))

    digits_size = 4
    digits_chars = string.digits

    print(name)

    keyboard.write(name)

    ###PASSWORD###
    keyboard.press_and_release("tab")
    time.sleep(1)

    characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

    def generate_random_password():
        ## length of password from the user
        length = 12

        ## shuffling the characters
        random.shuffle(characters)
            
        ## picking random characters from the list
        password = []
        for i in range(length):
            password.append(random.choice(characters))

        ## shuffling the resultant password
        random.shuffle(password)

        ## converting the list to string
        ## printing the list
        print("".join(password))
        keyboard.write(password)
            
        ###CONFIRM PASSWORD###
        time.sleep(2)
        keyboard.press_and_release("tab")
        keyboard.write(password)

    time.sleep(1)

    ## invoking the function
    generate_random_password()

    #DATE OF BIRTH REG#
    keyboard.press_and_release("tab")

    dayofbirth = str(random.randint(1, 28))

    keyboard.write(dayofbirth)

    keyboard.press_and_release("tab")
    time.sleep(1)

    repeat = random.randint(1, 12)
    for i in range(0, repeat):
        keyboard.press_and_release("down arrow")
    time.sleep(1)

    keyboard.press_and_release("tab")
    time.sleep(1)

    yearofbirth = str(random.randint(1950, 2001))
    keyboard.write(yearofbirth)

    #press tab 3 times!#
    keyboard.press_and_release("tab")
    time.sleep(0.25)
    keyboard.press_and_release("tab")
    time.sleep(0.25)
    keyboard.press_and_release("tab")

    time.sleep(1)
    keyboard.press_and_release("enter")

    for i in range(1, 13):
        time.sleep(0.25)
        keyboard.press_and_release("tab")
        
    time.sleep(1)

    keyboard.press_and_release("ctrl+v")

    time.sleep(1)

    #repeat tab for 4 times
    keyboard.press_and_release("tab")
    time.sleep(0.25)
    keyboard.press_and_release("tab")
    time.sleep(0.25)
    keyboard.press_and_release("tab")
    time.sleep(0.25)
    keyboard.press_and_release("tab")

    time.sleep(1)
    keyboard.press_and_release("enter")

    time.sleep(2)


    ###captcha skip###
    time.sleep(5)
    keyboard.press_and_release("tab")
    time.sleep(1)
    keyboard.press_and_release("enter")

    time.sleep(1)
    repeatam = random.randint(1, 6)
    for i in range(repeatam):
        keyboard.press_and_release("tab")
    keyboard.press_and_release("enter")

    #READING EMAIL FOR CODE#
    window_before = driver.window_handles[0]
    time.sleep(1)
    driver.switch_to.window(window_before)

    time.sleep(2)

    #COPYING CODE#
    time.sleep(10)
    #sleeping for email to load correctly#

    pyautogui.moveTo(879, 855)
    pyautogui.mouseDown()
    time.sleep(0.5)
    pyautogui.moveTo(936, 810)
    pyautogui.mouseUp()

    #copy code#
    keyboard.press_and_release("ctrl + c")
    time.sleep(2)

    driver.switch_to.window("tab2")
    time.sleep(1)

    #pasting code#
    pyautogui.moveTo(834, 542)
    pyautogui.click()

    keyboard.press_and_release("ctrl + v")

    time.sleep(5)

    ###NEW TAB###
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
    time.sleep(3)

    #LOADING TWITCH#

    followsite = twitchsite + usertofollow
    driver.get(followsite)
    time.sleep(5)
    #VERIFIED

    #FOLLOW#
    pyautogui.moveTo(1733, 759)
    time.sleep(1)
    pyautogui.click()

    #SHOW LOGIN#
    logfollow = "Following User: " + usertofollow
    print(logfollow)
    time.sleep(1)
    logname = "Username: " + name
    print(logname)

    time.sleep(5)
    driver.quit()
    time.sleep(5)

#FINISHED#
print("DONE")
log = open("Accounts.txt", a)
log.write(logname)
log.write("\n")
f.write(logfollow)
f.write("\n")
time.sleep(2)
