import requests
from bs4 import BeautifulSoup
import re # Importing regular expression module
def top_trending():
        url='https://in.reuters.com/news/top-news'
        r=requests.get(url) # The very old get function
        soup=BeautifulSoup(r.content,'html.parser') #Getting content
        links=soup.find_all(href=re.compile('/article/')) #getting every link which has the word article
        for i in links:
                print "->"+i.text #printing out text of the blockquote
top_trending() #Calling the function
