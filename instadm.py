from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from constants import username, instagram_home, user_secret, message


def path():
    global chrome
    # starts a new chrome session
    chrome = webdriver.Chrome('./chromedriver')


def url_name(url):
    chrome.get(url)
    time.sleep(4)   # we can be conservative with these sleep timers because it only happens once & is essential


def login(logged_in_user, logged_in_users_pw):
    # finds the username box
    usern = chrome.find_element_by_name("username")
    usern.send_keys(logged_in_user)

    # finds the password box
    passw = chrome.find_element_by_name("password")
    passw.send_keys(logged_in_users_pw)
    passw.send_keys(Keys.RETURN)
    time.sleep(4)  # we can be conservative with these sleep timers because it only happens once & is essential

    # Finding Not Now button
    notk = chrome.find_element_by_class_name("yWX7d")
    notk.click()
    time.sleep(4)  # we can be conservative with these sleep timers because it only happens once & is essential

    # Finding Not Now button #2
    notk2 = chrome.find_element_by_class_name("HoLwm")
    notk2.click()
    time.sleep(4)   # we can be conservative with these sleep timers because it only happens once & is essential
    # CONGRATS, YOU ARE LOGGED IN!!


def send_message(contestant):
    inbox_icon = chrome.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a')
    inbox_icon.click()
    time.sleep(.5)  # all these sleeps need to be cleaned.. they are just to throttle speed for now

    send_message_button = chrome.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div/div[3]/div/button')
    send_message_button.click()
    time.sleep(3)

    # type users name into the dm prompt
    who_you_tryna_dm = chrome.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/div[1]/div/div[2]/input')
    who_you_tryna_dm.send_keys(contestant)

    time.sleep(4)  # all these sleeps need to be cleaned.. they are just to throttle speed for now
    search_result_dm = chrome.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/div[2]/div[2]/div/div[3]/button/div')
    search_result_dm.click()
    time.sleep(.5)  # all these sleeps need to be cleaned.. they are just to throttle speed for now

    # click next
    next_button = chrome.find_element_by_xpath('/html/body/div[6]/div/div/div[1]/div/div[2]/div/button/div')
    next_button.click()
    time.sleep(2)  # all these sleeps need to be cleaned.. they are just to throttle speed for now

    message_input = chrome.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
    message_input.send_keys(message)

    message_input.send_keys(Keys.RETURN)

    time.sleep(.5)  # all these sleeps need to be cleaned.. they are just to throttle speed for now


def login_to_media_account():
    path()
    time.sleep(1)  # all these sleeps need to be cleaned.. they are just to throttle speed for now
    url_name(instagram_home)
    login(username, user_secret)

if __name__ == '__main__':
    login_to_media_account()

    for contestant_ig_name in ["jeffwhenderson"]:
        # visit their page and send a message
        # url_name(instagram_home)
        send_message(contestant_ig_name)

    chrome.close()
