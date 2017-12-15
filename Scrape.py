from urllib2 import urlopen as uReq
from bs4 import BeautifulSoup as soup
import time 
import requests
from twilio.rest import TwilioRestClient


url = 'https://postmates.com/los-angeles'
account_sid = #Your SID
auth_token = #Put Auth token Here
twilio_phone_number = #Put Twilio phone number here
my_phone_number = #

text = raw_input("Would you like to connect a Twilio account to get a text message if there is a change?")
if text.lower() == 'y' or text.lower() == 'yes':
	account_sid = raw_input("Twilio account sid")
	auth_token = raw_input("Twilio authentication token")
	twilio_phone_number = raw_input("+" + "twilio phone number")
	my_phone_number = raw_input("+" + "Your phone number")



# this is an optional parameter for the frequency you wish 
alloted_time  = 10
#this is an optional parameter for the duration you wish the search to occur, the default is one day
duration = 86400

#the following bit is for use in the while loop 
iteration = 0; 
my_url = 'https://www.google.com'
#optional parameters of time can be changed here:

#connection 
def main():
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()


    page_soup = soup(page_html, "html.parser")
    href_tags = page_soup.find_all(href=True)
    initial_result = len(href_tags)
    time.sleep(10)
    href_tags = page_soup.find_all(href=True)
    if new_result - initial_result == 0:
        print ("no change")
    elif new_result - initial_result > 0 or new_result - initial_result < 0:
        print("change")
    else:
        print ("nothing noticed")
   


while iteration < duration / alloted_time:
    main()
    time.sleep(alloted_time)
    iteration += 1
