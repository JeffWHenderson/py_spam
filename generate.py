import math
import instaloader

from constants import username, user_secret, winnerName, post_short_code

L = instaloader.Instaloader()
L.login(username, user_secret)

def get_all_users_that_commented():
    post = instaloader.Post.from_shortcode(L.context, post_short_code)

    commenters_array = []

    for comment in post.get_comments():
        instagram_user = comment.owner.username
        if instagram_user not in commenters_array:
            if instagram_user != winnerName:
                commenters_array.append(instagram_user)

    return commenters_array


def split_array_into_text_files(num, commenters):
    number_of_users_per_file = len(commenters) / num
    index = 0

    for x in range(num):  # run a loop num times
        f = open("usernames_" + str(x + 1) + ".txt", "x")

        for y in range(0, math.floor(number_of_users_per_file)):
            f.write(commenters[index] + "\n")
            index = index + 1


if __name__ == '__main__':
    commenters = get_all_users_that_commented()
    split_array_into_text_files(4, commenters)
