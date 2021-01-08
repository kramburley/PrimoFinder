# Import requests (to download the page)
import requests

# Import BeautifulSoup (to parse what we download)
from bs4 import BeautifulSoup

# Import Time (to add a delay between the times the scape runs)
import time

# Import smtplib (to allow us to email)
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Import random for random number addition to timedelay
import random

import sys

# a script to monitor GenshinImpact's website promo code page for any changes. If something is added on the table on GI's promo page, send email to recipients
url = "https://www.gensh.in/events/promotion-codes"
un = '' #add email username here
pwd = '' #add email password here
timedelay = 300 + random.randint(1, 1800);
# timedelay = 5

recipients = ["mark.tan@alianz.ca", 'lorenbeyd@gmail.com', 'ariston.ricky@gmail.com']

newCode = []

def grabWebContent(url):
    # set the headers to seem like we are a browser
    headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; SM-G928X Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36'}
    # download the webpage
    response = requests.get(url, headers=headers)
    # parse the downloaded homepage and grab all text
    soup = BeautifulSoup(response.text, "lxml")
    
    return soup


def checkNewCodes():
    soup = grabWebContent(url)
    table = soup.find_all('table')[0].tbody.find_all('tr')

    for i in table:
        status = i.find_all('td')[1].text.replace(' ', '')
        code = i.find_all('td')[3].text.replace(' ', '')

        if status.lower() != 'yes': 
            newCode.append(code)
    
    return newCode


def notify(receiver_email, promoCodes):
    # create an email message with just a subject line,
    msg = 'GenshinScanner: NEW PROMOCODE RELEASED. CHECK {} !'.format(url)
    bmsg = 'NEW PROMO CODES: \n\n'
    for i in promoCodes:
        bmsg += i + '\n'
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = un
    message['To'] = receiver_email
    message['Subject'] = msg   #The subject line
    
    #The body and the attachments for the mail
    message.attach(MIMEText(bmsg, 'plain'))
    
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(un, pwd) #login with mail_id and password
    text = message.as_string()
    session.sendmail(un, receiver_email, text)
    session.quit()
    print('Notify Mail Sent to: ', receiver_email)


def run():
    # tracks number of times the program has ran
    executioncounter = 0
    
    # while this is true (it is true by default),
    while True:    
        # if the list of codes does not contain anything, continue
        newCodes = checkNewCodes()
        if len(newCodes) == 0:
            executioncounter += 1
            sys.stdout.write('\r{}'.format(executioncounter))
            sys.stdout.flush()
            # wait before continuing script
            time.sleep(timedelay)
            # continue with the script
            continue
            
        # but if the word "Google" occurs any other number of times,
        else:
            # notify list of users
            for val in recipients:
                notify(val, newCodes)
            break

run()



# TODO: CREATE A DUMMY EMAIL AND USE THAT
# TODO: Check if actually counts number of word occurence or just checks if word exists or not. if word exist check only, think of another approach.
# TODO: test by running program atleast once
# TODO: add a random number of minutes to make the check less robotic in MiHoYo's eyes.