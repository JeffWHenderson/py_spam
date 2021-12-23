import instaloader
import time
from selenium.webdriver import chrome
from instadm import path, url_name, send_message, login
from constants import username, instagram_home, user_secret, winnerName, post_short_code, message

L = instaloader.Instaloader()
L.login(username, user_secret)

def get_all_users_that_commented():
    post = instaloader.Post.from_shortcode(L.context, post_short_code)

    commenters = []

    i = 0
    for comment in post.get_comments():
        instagram_user = comment.owner.username
        if instagram_user not in commenters:
            if instagram_user != winnerName:
                commenters.append(instagram_user)
        i += 1

        if i == 50:
            return commenters
            break

    return commenters

def login_to_media_account():
    path()
    time.sleep(1)
    url_name(instagram_home)
    login(username, user_secret)

if __name__ == '__main__':
    # commenters = get_all_users_that_commented()

    login_to_media_account()

    # commenters:
    for user in ["sethbenton"]:
        # visit their page and send a message
        # url_name(instagram_home)
        send_message(user, message)

    chrome.close()
