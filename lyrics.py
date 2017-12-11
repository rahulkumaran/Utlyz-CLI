import requests
from bs4 import BeautifulSoup
url='https://search.azlyrics.com/search.php?q='
req=raw_input('Give me the name of the song: ')   
def get_url(req):
    req_url=url+req.replace(' ','+')
    r=requests.get(req_url)
    soup=BeautifulSoup(r.content,'html.parser')
    temp=str(soup.findAll(class_='text-left visitedlyr')[0])
    song_url=temp.split('href="')[1]
    song_url=song_url.split('"')[0]
    return song_url
def get_lyrics():
    s=requests.Session()
    s.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
    r=s.get(get_url(req))
    soup=BeautifulSoup(r.content,'html.parser')
    temp=str(soup.findAll(class_='row'))
    temp=temp.replace('//n','')
    temp=temp.split('<br/>')
    print temp[2].split('\\r')[-1]
    for i in temp:
        if '<' in i:
            pass
        else:
            print i

get_lyrics()



