# High light from here 
from urllib2 import urlopen as uReq
from bs4 import BeautifulSoup as soup
import time 

# this is an optional parameter for the frequency you wish 
alloted_time  = 10
#this is an optional parameter for the duration you wish the search to occur, the default is one day
duration = 86,400

# the following bit is for use in the while loop 
iteration = 0; 
my_url = 'http://deeplearning.net/'
#optional parameters of time can be changed here:

# connection 
def main():
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()


    page_soup = soup(page_html, "html.parser")
    element_of_focus = page_soup.h1
    var = len(element_of_focus)
    if var == 1:
        print ("no change")
    elif var > 1:
        print ("The inital words of this website have changed")
    else:
        print ("no change that we have noticed, p.s. 'we' are the evil umpire")
    



while iteration < duration / alloted_time:
    main()
    time.sleep(alloted_time)
    iteration += 1
# To Here and CTRL + C 
