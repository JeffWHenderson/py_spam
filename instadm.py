from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time


def path():
    global chrome

    # starts a new chrome session
    chrome = webdriver.Chrome('./chromedriver')  # Add path if required


def url_name(url):
    chrome.get(url)
    # adjust sleep if you want
    time.sleep(2)


def login(username, your_password):
    # finds the username box
    usern = chrome.find_element_by_name("username")
    # sends the entered username
    usern.send_keys(username)

    # finds the password box
    passw = chrome.find_element_by_name("password")
    # sends the entered password
    passw.send_keys(your_password)

    # press enter after sending password
    passw.send_keys(Keys.RETURN)
    time.sleep(4)

    # Finding Not Now button
    notk = chrome.find_element_by_class_name("yWX7d")
    notk.click()
    time.sleep(3)

    # Finding Not Now button #2
    notk2 = chrome.find_element_by_class_name("HoLwm")
    notk2.click()
    time.sleep(3)


def send_message(username, message):
    inbox_icon = chrome.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a')
    inbox_icon.click()
    time.sleep(.5)
    send_message_button = chrome.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div/div[3]/div/button')
    send_message_button.click(.5)

    # type users name into the dm prompt
    ActionChains(chrome).send_keys(username)

    # click next
    next_button = chrome.find_element_by_xpath('/html/body/div[6]/div/div/div[1]/div/div[2]/div/button/div')
    next_button.click()
    # mbox = chrome.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
    for line in message.split("\n"):
        ActionChains.send_keys(line)
        ActionChains(chrome).key_down(Keys.SHIFT).key_down(Keys.RETURN).key_up(Keys.RETURN).key_up(Keys.SHIFT).perform()

    ####******* WARNING **********#####
    ### IF YOU UNCOMMENT THE BELOW LINE THE MESSAGES WILL SEND TO USER
    # mbox.send_keys(Keys.RETURN)

    time.sleep(.5)
