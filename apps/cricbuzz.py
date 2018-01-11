from bs4 import BeautifulSoup
import mechanize
import click

'''
A command line application that allows you to perform tasks
from the command line interface on Facebook. But only one
option can be used at a time and all options being used together
will not allow you to use the total functionality of this program.
'''

def find_soup(browser,url):
	response = browser.open(url)
	return BeautifulSoup(response,'html.parser')

@click.command()

@click.option('--score',is_flag=True,help='Gives score summary of all ongoing matches.')

@click.option('--schedule',is_flag=True,help='Gives list of upcoming matches in that particular month.')

def cli(score,schedule):
	browser = mechanize.Browser()
	browser.set_handle_robots(False)	#Allows everything to be written only
	cookies = mechanize.CookieJar()
	browser.set_cookiejar(cookies)
	browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.41 Safari/534.7')]
	browser.set_handle_refresh(False)	#Sometimes hangs without this

	if(score):		#Called after score option is called
			soup = find_soup(browser,'http://www.cricbuzz.com/cricket-match/live-scores')	#Gets HTML of entire page
			score_box = soup.find_all('div',attrs={'class':'cb-lv-scrs-col text-black'})	#Navigating to where the score is available in the page
			#score_box_narrow = soup.find_all('span',attrs={'class':'text-bold'})		#Narrowing down search to where the score is avaiable
			score_box_num = []
			click.echo("\nThe scores of all matches being played currently is displayed below:\n")
			num=1
			for i in score_box:		#To get the score of all live matches and recently done matches
				score_box_num += [i.text]
				click.echo("%d) %s\n"%(num,i.text))
				click.echo("----------------------------------------------------------")
				num+=1

	if(schedule):
			soup = find_soup(browser,'http://www.espncricinfo.com/ci/engine/match/index.html?view=calendar')
			schedule_box = soup.find('section',attrs={'class':'calendar-match-list'})
			schedule_box_narrow = schedule_box.find_all('section',attrs={'class':'calendar-match-day'})
			for i in schedule_box_narrow:
					click.echo(i.text)
					click.echo('--------------------------------------------------')






