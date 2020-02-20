import hashlib
import urllib2
import random
import time
import smtplib

# Be sure to allow less secure apps in your google account
# Url to be scraped
url_search = "http://experienciasblack.lanacion.com.ar"
# Pattern to search
pattern = "ahora</h3>"

# Your gmail address, just the user, dont type @gmail.com
gmail_address = " " 

# Your password
gmail_password = " " 

# To the address you want to send the mail
to_address = " "

# Mail content
mail_content = " " 


# Time between checks in seconds
sleeptime = 60



def getHash(url):
    '''Function that given an url returns its HTML code'''
    
    # User agent to open the url
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', user_agent)]
    response = opener.open(url)
    the_page = response.read()
	
    return the_page

current_page = getHash(url_search)

while 1: # Run forever
    if getHash(url_search).find(pattern) == -1: # No pattern
        print("Patter not found")
    else: # Pattern found
        #Google API to send the mail
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(gmail_address, gmail_password)
        server.sendmail(gmail_address+"@gmail.com", to_address, mail_content)
        server.close()
        print("Mail has been sent")
    time.sleep(sleeptime)
