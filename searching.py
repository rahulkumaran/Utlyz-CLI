import mechanize
import google
import click
import wikipedia

'''
This is a program which gives you the ability to search
for topics on google and get their respective links from
the CLI. You can just click on link to open the webpage.
The program also helps you search wikipedia for a topic.
The page results are displayed on the command line itself.
'''

@click.command()

@click.option('--srch',is_flag=True,help='Searches the results related to the topic you enter')

@click.option('--wiki',is_flag=True,help='Gives you the wikipedia page for the topic')

def cli(srch,wiki):
	if(srch):
		browser = mechanize.Browser()
		browser.set_handle_robots(False)	#Allows everything to be written
		cookies = mechanize.CookieJar()
		browser.set_cookiejar(cookies)
		browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.41 Safari/534.7')]
		browser.set_handle_refresh(False)	#Sometimes hangs without this
		query = raw_input("Enter the topic you want to search about: ") 
		for link in google.search(query, tld="com", num=10, stop=1, pause=2):	#To get the first few links related to the topic.
			print link	#Click on the displayed link to open page on browser
	if(wiki):
		wiki_topic = raw_input('Enter the topic you want to read about: ') #To get search topic from user
		result = wikipedia.page(title=wiki_topic,auto_suggest=True,redirect=True, preload=False) #searches the best results for the topics
		wiki_content = result.content #stores content of the page
		print wiki_content
