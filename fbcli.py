from bs4 import BeautifulSoup
import mechanize
import click

'''
A command line application that allows you to perform tasks
from the command line interface on Facebook. But only one
option can be used at a time and all options being used together
will not allow you to use the total functionality of this program.

'''

email = raw_input('Enter your Email ID: ')
pwd = raw_input('Enter your password: ')

def authenticate(browser,url,email,pwd):
	browser.open(url)
	browser.select_form(nr = 0)       #This is login-password form -> nr = number = 0
	browser.form['email'] = email
	browser.form['pass'] = pwd
	response = browser.submit()
	return BeautifulSoup(response,'html.parser')

@click.command()

@click.option('--fr',is_flag=True,help='Gives you the number of friend requests you have not seen yet') 

@click.option('--msg',is_flag=True,help='Gives you the number of unread messages')

@click.option('--notifs',is_flag=True,help='Gives you the number of unseen notifications')

@click.option('--bdays',is_flag=True,help='Gives the names of those who have their birthdays today')


def cli(fr,msg,notifs,bdays):
	browser = mechanize.Browser()
	browser.set_handle_robots(False)	#Allows everything to be written
	cookies = mechanize.CookieJar()
	browser.set_cookiejar(cookies)
	browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.41 Safari/534.7')]
	browser.set_handle_refresh(False)	#Sometimes hangs without this
	bday_people_links=[] 		#List to store profile links of people who have their birthdays today
	bday_people_names=[]
	i=1
	try:
		if(bdays):
			url = 'http://www.facebook.com/events/birthdays/'
			soup = authenticate(browser,url,email,pwd)	#Parses the html and stores in 'soup'
			bday_box = soup.find('div',attrs={'class':'_4-u2 _tzh _fbBirthdays__todayCard _4-u8'})	#Finds the html with the div tags and given attributes 
			bday_box_narrow = bday_box.find_all('a',attrs={'data-hovercard-prefer-more-content-show':'1'})		#Finds all a tags with the given attirbute. This will be the list of bdays
			click.echo("%d people have their birthdays today :\n"%(len(bday_box_narrow)))
			for a in bday_box_narrow:
				print str(i)+')',a.text		#prints names of people who have their birthdays today
				bday_people_names += [a.text]		#stores names of people who have their birthdays today
				bday_people_links += [a.get('href')]		#stores links of profiles of people have their bdays today
				i+=1
		else:
			url = 'http://www.facebook.com/login.php'
			soup = authenticate(browser,url,email,pwd)	#Parses the html and stores in 'soup'
			if(fr):			#To find number of new friend request
				fr_num_box = soup.find('span',attrs={'id':'requestsCountValue'})		#Finds span tags with the given ID
				click.echo("You have %s new friend requests" %(fr_num_box.text))		#Displays and gives the string between the span tags (<span>...</span>)
			if(msg):		#To find number of unread messages
				msg_num_box = soup.find('span',attrs={'id':'mercurymessagesCountValue'})
				click.echo("You have %s unread messages" %(msg_num_box.text))
			if(notifs):		#To find the number of unseen notifications
				notifs_num_box = soup.find('span',attrs={'id':'notificationsCountValue'})
				click.echo("You have %s unread notifications"%(str(int(notifs_num_box.text)+1)))
	except AttributeError:
		click.echo("Either the password or email id you've entered is wrong")
