from bs4 import BeautifulSoup
import mechanize
import click


def find_soup(browser,url):
	response = browser.open(url)
	return BeautifulSoup(response,'html.parser')

@click.command()

@click.option('--scores',is_flag=True,help="Gives you the scores of the matches!")

@click.option('--transfers',is_flag=True,help="Gives latest rumours about transfers")

def cli(scores, transfers):
	browser = mechanize.Browser()
	browser.set_handle_robots(False)	#Allows everything to be written
	cookies = mechanize.CookieJar()
	browser.set_cookiejar(cookies)
	browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.41 Safari/534.7')]
	browser.set_handle_refresh(False)	#Sometimes hangs without this
	if(scores):		#Called after score option is called
		soup = find_soup(browser,'http://www.goal.com/en-in/live-scores')	#Gets HTML of entire page
		score_box = soup.find_all('div',attrs={'class':'match-main-data'})	#Navigating to where the score is available in the page
		click.echo("\nThe scores of all matches being played currently is displayed below:")
		click.echo("--------------------------------------------------------------------")
		for i in score_box:		#To get the score of all live matches and recently done matches
			print i.text
			click.echo("--------------------------------------------------------------------")
		click.echo("\n\nNOTE: ALL THE MATCH TIMINGS ARE IN GMT\n\n")
	if(transfers):
		soup = find_soup(browser,'http://www.goal.com/en-us/transfer-rumours/1')	#Gets HTML of entire page
		rumours = soup.select(".transfer-card__desc p")
	click.echo("\nThe latest Transfer news & rumours are displayed below:")
	click.echo("--------------------------------------------------------------------")
	for i in rumours:
		print("->"+i.text)
		click.echo("--------------------------------------------------------------------")
