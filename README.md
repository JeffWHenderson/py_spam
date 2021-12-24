# WELCOME TO THE JUNGLE  

## PYGRAM, HOW TO, AND STUFF

###UPDATE THE constants.py

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
* you've updated the constants file 
  * i know, there are better ways to do this, but it is a POC
* run ``python3 generate.py``, Grab a coffee, this will take some time to run. It will generate 4 files of instagram users that commented on a specific post
  * splitting these so we can run multiple dm programs. 
  * 4 is the default because why not?
* run ``python instadm.py``
* when prompted you can enter username_1.txt
  * or username_2.txt (the world is your oyster) 
* all the users in username_1.txt will be sent a DM with the message you wrote in constants

* 
* **TO STOP THE PROGRAM:** press CONTROL + C

### TroubleShooting
* I expect something annoying will be if you have a different version of chrome than the chrome driver. Potentially you will need to download the chromedriver that matches your google chrome version
* This is a POC and needs proper quality control before it can be a real boy
* I feel like this README sounds snarky... I'm sorry, I am cooler than this documentation can express