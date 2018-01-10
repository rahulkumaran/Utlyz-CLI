import requests
from bs4 import BeautifulSoup
import re # Importing regular expression module
import click

@click.command()
@click.option("--trending",is_flag=True,help='Gives the trending news topics!')
def cli(trending):
        if(trending):
                url='https://in.reuters.com/news/top-news'
                r=requests.get(url) # The very old get function
                soup=BeautifulSoup(r.content,'html.parser') #Getting content
                links=soup.find_all(href=re.compile('/article/')) #getting every link which has the word article
                for i in links:
                    if(i.text != 'Continue Reading'):
                        if(i.text != ""):
                            print("->" + i.text) #printing out text of the blockquote
