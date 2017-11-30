# p4mawpup---LucianH.

First make sure Python 2.7.14 is installed 
Next download Anaconda; 32/64 depending on OS 
Create and open an virtual enviorment by entering in the command terminal c:\Python27\Scripts\virtualenv -p c:\Python27\python.exe .lpvenv
then activate the virtualenv by entering .lpvenv\Scripts\activate 
Open CMD and type "pip install bs4"
Now inside the virtual env type "python" hit enter and the python's idle command prompt should appear.
Note: this is to test every line to make sure that it works first. 
Open a new editor file in your editor of choice i.e. notepad ++
Set the notepad ++ language to python and also go into prefrences and then languages and change the tab options to 4 spaces not the default.
Now Copy and paste the following code into the new file and save as a .py file inside of your .lpvenv/Scripts

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

Once that's complete, run the .py file under the virtual env directory or in the python idle command prompt as "python file_name.py"

Mileage may vary 
