from bs4 import BeautifulSoup
import mechanize
import click

@click.command()

@click.option('--fr',is_flag=True,help='Gives you the number of friend requests you have not seen yet') 

@click.option('--msg',is_flag=True,help='Gives you the number of unread messages')

@click.option('--notifs',is_flag=True,help='Gives you the number of unseen notifications')

def cli(fr,msg,notifs):
	email = raw_input("Enter Email ID: ")
	pwd = raw_input("Enter Password: ")
	browser = mechanize.Browser()
	browser.set_handle_robots(False)	#Allows everything to be written
	cookies = mechanize.CookieJar()
	browser.set_cookiejar(cookies)
	browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.41 Safari/534.7')]
	browser.set_handle_refresh(False)	#Sometimes hangs without this

	url = 'http://www.facebook.com/login.php'
	browser.open(url)
	browser.select_form(nr = 0)       #This is login-password form -> nr = number = 0
	browser.form['email'] = email
	browser.form['pass'] = pwd
	response = browser.submit()
	#print response.read()
	soup = BeautifulSoup(response,'html.parser')	#Parses the html and stores in 'soup'
	try:
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


