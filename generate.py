import instaloader
from constants import username, user_secret, winnerName, post_short_code

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


if __name__ == '__main__':
    get_all_users_that_commented()
