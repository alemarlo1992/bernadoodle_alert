import requests
from os import environ
import time 
from bs4 import BeautifulSoup
from datetime import datetime

from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
import logging


def puppy_alert():
    """Send text when puppy is availble using Twilio API."""
    account_sid = environ['TWILIO_ACCOUNT_SID']
    auth_token = environ['TWILIO_AUTH_TOKEN']

    TWILIO_NUMBER = '+12058720099'

    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                            body='Puppy is availble! go to https://gailsdoodles.com/current-litters',
                            from_=TWILIO_NUMBER,
                            to='+16192895400'
                     )
    print(message.sid)

    
def checking_pup():
    """Script that checks gailsdoodles.com for desired pup"""
    available = False

    while True: 
        dad = environ.get("DAD", "Finley")
        mom = environ.get("MOM", "Holly")
        print(f"checking with DAD {dad} and Mom: {mom}")
        headings = []

        get_page = requests.get('https://gailsdoodles.com/current-litters')
        print("After get_page")
        page_details = BeautifulSoup(get_page.text, 'html.parser')
        print("After get_details:")
        for headlines in page_details.find_all("h1"):
            headings.append(headlines.text.strip())


        for h1 in headings:
            print("Each h1:", h1, type(h1), len(h1))
            print("Checking Mom:",mom, h1 == mom)
            print("Checking Dad:",dad, h1 == dad)

            if h1 == mom or h1 == dad: 
                print("There was a match with heading:", h1)
                available = True 
        print("After headings", available)
        if available == True:
            print("Puppy available")
            # puppy_alert() #send text messege notification
            break
        else: 
            time.sleep(10) #sleep for 3 min 

