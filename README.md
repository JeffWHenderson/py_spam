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

#RUN on the commandline
## example flow: 
* run ``python3 generate.py``, this will take some time but generate 4 files.
* run ``python instadm.py``
* when prompted you can enter username_1.txt
* all the users in username_1.txt will be sent a file

### TroubleShooting
I expect something annoying will be if you have a different version of chrome than the chrome driver. Potentially you will need to download the chromedriver that matches your google chrome version