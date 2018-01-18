from urllib2 import urlopen as uReq
from bs4 import BeautifulSoup as soup
import time 
import twilio #the module importation should be updated.
import twilio.rest 


url = 'https://postmates.com/los-angeles'
account_sid = 'AC05a19e314e2e0a36da9d8966556c359c'
auth_token = 'Whatever'
twilio_phone_number = 'Host'
my_phone_number = 'Clients'



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
    new_result = len(href_tags)
    print (new_result - initial_result) # tell you how many links were added or removed 
    if new_result - initial_result == 0:
        print ("no change")
     #implementation of twilio...
    elif new_result - initial_result < 0 or new_result - initial_result > 0:
        client = twilio.rest.Client('AC05a19e314e2e0a36da9d8966556c359c', '8cf175a0d0d3587e9a8ceece40bfa2c6')
    
        client.messages.create(
            body="Google just changed something on their homepage",
            to=my_phone_number,
            from_=twilio_phone_number
            )

    else:
        print ("nothing noticed")
   


while iteration < duration / alloted_time:
    main()
    time.sleep(alloted_time)
    iteration += 1
