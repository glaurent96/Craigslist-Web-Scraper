#!/usr/bin/python3.5

from bs4 import BeautifulSoup
from urllib.request import urlopen
import math
import csv
import smtplib
import os
import filecmp
from email.mime.text import MIMEText

body = '\n'
hits = []

#Obtain user input for what to search for
#userItem = input("Enter item you are looking for")
userItem = "Vintage"
#userCity = input("Enter city you want the item to be in")
userCity = "chico"
#numHits = int(input("Enter maximum number of listings you want to see")
numHits = 10

#URL of the page we are trying to scrape
baseURL = 'https://chico.craigslist.org/search/ata/'

#Obtain the html code for the page below
sauce = urlopen(baseURL).read()

#My gmail login info, because I am sending the email with my account
gmail_user = 'glaurent@mail.csuchico.edu'
gmail_password = '***************'

#Send updates to my email address
sent_from = gmail_user
to = ['gadipraja@mail.csuchico.edu']
subject = 'GG'

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

#Send the email and report an error if it doesn't work 
try:
  server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
  server.ehlo()
  server.login(gmail_user, gmail_password)
  server.sendmail(sent_from, to, email_text)
  server.close()
except:
  print('ERROR: Something went wrong while sending the email')

