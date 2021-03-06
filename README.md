# PrimoFinder

Created a console app to check Genshin Impact's website for new promo codes and send out emails to those registered.

Pre-requisites:

requests
BeautifulSoup
time
smtplib
random
sys
lxml




Things to do before running:

1.) update the following variables:

      (line 21) un: username for your email 
      
      (line 22) pw: password for your email 
      
      (line 27) recipients: add as many email addresses to the list as you want i.e. ['sample@email.com', 'sample2@email.com']
      
      
2.) compile by typing on the commandline pyinstaller --oneflie .\primogemfinder.py

3.) run the created file under dist folder and wait for an email for new promocodes!

NOTE:
When running the app and you receive an authentication error, allow less secure apps in your google account.
https://www.google.com/settings/security/lesssecureapps


Identified Limitations:

1.) Once promocode is detected and app sends an email. App shutsdown and user has to restart the program.

2.) Once a new promo code is detected and used to send out email. Upon restarting program, will perform the same way until either MiHoYo decides to change the status of promocode to 'NO' OR user updates "usedCodes" list to include most recently used code.
