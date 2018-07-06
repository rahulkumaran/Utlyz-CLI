import mechanize
from googlesearch import search
import click
import wikipedia

@click.command()

@click.option('--google',is_flag=True,help='Searches the results related to the topic you enter')

@click.option('--wiki',is_flag=True,help='Gives you the wikipedia page for the topic')

def cli(google,wiki):
	browser = mechanize.Browser()
	browser.set_handle_robots(False)	#Allows everything to be written
	cookies = mechanize.CookieJar()
	browser.set_cookiejar(cookies)
	browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.41 Safari/534.7')]
	browser.set_handle_refresh(False)	#Sometimes hangs without this
	if(google):
		query = raw_input("Enter the topic you want to search about: ")
		for link in search(query, tld="co.in", num=10, stop=1, pause=2):
			print link
	if(wiki):
		wiki_topic = raw_input('Enter the topic you want to read about: ')
		result = wikipedia.page(title=wiki_topic,auto_suggest=True,redirect=True, preload=False)
		wiki_content = result.content
		print wiki_content
