## how to run

UPDATE THE constants.py
**username:** = add the username for the instagram account

**user_secret:** = add the pw for the instagram account

**instagram_home:** = always is 'https://instagram.com/'

**winnerName:** add winner name so they will be excluded from emails

**post_short_code:** add shortcode (CW9Fh_As_1g is the short code for https://www.instagram.com/p/CW9Fh_As_1g/)

**message:** the personalized message you want to send them 


## !!REQUIRED!!
Python3

##RUN on the commandline
generate 4 files with all the names of people that commented on a post:
  ``python3 generate.py``

Send a personalized message to all users given a file:
  ``python3 instadm.py -f EXAMPLE_FILENAME.txt``

### TroubleShooting
I expect something annoying will be if you have a different version of chrome than the chrome driver. Potentially you will need to download the chromedriver that matches your google chrome version