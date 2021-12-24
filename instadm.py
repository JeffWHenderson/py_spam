from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from constants import username, instagram_home, user_secret, message


def path():
    global chrome
    # starts a new chrome session
    chrome = webdriver.Chrome('./chromedriver')


def go_to_url(url):
    chrome.get(url)
    time.sleep(4)   # we can be conservative with these sleep timers because it only happens once & is essential


def login(logged_in_user, logged_in_users_pw):
    # finds the username box
    usern = chrome.find_element(By.NAME, "username")
    usern.send_keys(logged_in_user)
    time.sleep(1)

    # finds the password box
    passw = chrome.find_element(By.NAME, "password")
    passw.send_keys(logged_in_users_pw)
    time.sleep(4)  # we can be conservative with these sleep timers because it only happens once & is essential
    passw.send_keys(Keys.RETURN)
    time.sleep(4)  # we can be conservative with these sleep timers because it only happens once & is essential

    # Finding Not Now button
    try:
        notk = chrome.find_element(By.CLASS_NAME, "yWX7d")
        notk.click()
        time.sleep(4)  # we can be conservative with these sleep timers because it only happens once & is essential
    except Exception as e:
        print("oh no!!! a message to " + contestant_ig_name + " failed")

    # Finding Not Now button #2
    try:
        notk2 = chrome.find_element(By.CLASS_NAME, "HoLwm")
        notk2.click()
        time.sleep(4)   # we can be conservative with these sleep timers because it only happens once & is essential
    except Exception as e:
        print("oh no!!! a message to " + contestant_ig_name + " failed")
    # CONGRATS, YOU ARE LOGGED IN!!


def send_message(contestant):
    inbox_icon = chrome.find_element(By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a')
    inbox_icon.click()
    time.sleep(.5)  # we can lower these sleep times. They are just to throttle speed for now

    send_message_button = chrome.find_element(By.XPATH, '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div/div[3]/div/button')
    send_message_button.click()
    time.sleep(3)

    # type users name into the dm prompt
    who_you_tryna_dm = chrome.find_element(By.XPATH, '/html/body/div[6]/div/div/div[2]/div[1]/div/div[2]/input')
    who_you_tryna_dm.send_keys(contestant)

    time.sleep(4)  # we can lower these sleep times. They are just to throttle speed for now
    search_result_dm = chrome.find_element(By.XPATH, '/html/body/div[6]/div/div/div[2]/div[2]/div[1]/div')
    search_result_dm.click()
    time.sleep(.5)  # we can lower these sleep times. They are just to throttle speed for now

    # click next
    next_button = chrome.find_element(By.XPATH, '/html/body/div[6]/div/div/div[1]/div/div[2]/div/button/div')
    next_button.click()
    time.sleep(2)  # we can lower these sleep times. They are just to throttle speed for now

    message_input = chrome.find_element(By.XPATH, '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
    message_input.send_keys(message)

    message_input.send_keys(Keys.RETURN)

    time.sleep(.5)  # we can lower these sleep times. They are just to throttle speed for now


def login_to_media_account():
    path()
    time.sleep(1)  # we can lower these sleep times. They are just to throttle speed for now
    go_to_url(instagram_home)
    login(username, user_secret)

if __name__ == '__main__':
    filename = input("what is the name of the file you want to read usernames from? ")
    login_to_media_account()

    f = open(filename, "r")
    count = 0

    while True:
        count += 1

        # Get next line from file
        contestant_ig_name = f.readline()

        if not contestant_ig_name:
            break

        try:
            send_message(contestant_ig_name.strip())
        except Exception as e:
            print("oh no!!! a message to " + contestant_ig_name + " failed")
            time.sleep(3)  # we can lower these sleep times. They are just to throttle speed for now
            go_to_url(instagram_home)
    
    # chrome.close()
    f.close()
