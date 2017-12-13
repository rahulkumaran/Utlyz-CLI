import requests
from bs4 import BeautifulSoup
import click


url='https://search.azlyrics.com/search.php?q='
req=raw_input('Give me the name of the song: ')

def get_url(req):
    '''
    This function is used to get the required url for the song
    '''
    req_url=url+req.replace(' ','+')
    r=requests.get(req_url)
    soup=BeautifulSoup(r.content,'html.parser')
    temp=soup.findAll(class_='text-left visitedlyr')     #For the link to the song lyrics
    for i in temp:
        i=str(i)
        i=i.split('href="')[1]
        i=i.split('"')[0]
        if '/lyrics/' in i:
            song_url=i
            #print song_url
            break
 #Modifications done to get it compatible with requests module
    return song_url

@click.command()

@click.option('--lyr',is_flag=True,help='Gives you the lyrics of a song of your choice')

def cli(lyr):
	if(lyr):
        s=requests.Session() #It is having so many redirects so use of session is helpful or we get an error
        s.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36' #Headers
        r=s.get(get_url(req)) #Session get similarl to requests.get()
        soup=BeautifulSoup(r.content,'html.parser')
        temp=str(soup.findAll(class_='row'))
        temp=temp.replace('\\n','')
        temp=temp.split('<br/>') #Modifications of source code to get our required outcome
        print temp[2].split('\\r')[-1]
        for i in temp:	#Loop is for modifying each string so that no junk appears except \n
        	if '<' in i:
        	    pass
        	else:
        	    print i
