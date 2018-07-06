from telegram.ext import CommandHandler, Updater
from telegram import *
import requests
import telepot
import re
import wikipedia
from bs4 import BeautifulSoup
import os
import mechanize




################################################################	FEW NECESSARY FUNCTIONS FOR THE BOT HERE	########################################################################


def get_url(args):
        '''
        This function is used to get the required url for the song
        '''
	url='https://search.azlyrics.com/search.php?q='
	for arg in args:			#will extract name from the argument list
		url += arg + "+"		#adding a space between the words
	r=requests.get(url)
	soup=BeautifulSoup(r.content,'html.parser')
	temp=soup.findAll(class_='text-left visitedlyr')     #For the link to the song lyrics
	for i in temp:				#gives the entire url to search
	    i=str(i)
	    i=i.split('href="')[1]
	    i=i.split('"')[0]
	    if '/lyrics/' in i:
	        url=i
	        break
     #Modifications done to get it compatible with requests module
	return url


def authenticate(browser,url,email,pwd):
	browser.open(url)
	browser.select_form(nr = 0)       #This is login-password form -> nr = number = 0
	browser.form['email'] = email
	browser.form['pass'] = pwd
	response = browser.submit()
	return BeautifulSoup(response,'html.parser')

################################################################	CODE FOR BOT FUNCTIONALITIES STARTS HERE	########################################################################


def start(bot,update):
	bot.sendChatAction(chat_id = update.message.chat_id, action = ChatAction.TYPING)
	#time.sleep(0.2)
	#print update.message.chat_id
	bot.sendMessage(chat_id = update.message.chat_id, text = '''
		Hey %s %s! Welcome to UtlyzMeBot! Type /help for more information regarding the functionalities of this particular bot. In short, this bot will help you search wiki, google, get news bulletins and what not from this particular chat window itself :D 
	''' %(update.message.from_user.first_name,update.message.from_user.last_name))


def fb(bot, update, args):
	browser = mechanize.Browser()
	browser.set_handle_robots(False)	#Allows everything to be written
	cookies = mechanize.CookieJar()
	browser.set_cookiejar(cookies)
	browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.41 Safari/534.7')]
	browser.set_handle_refresh(False)	#Sometimes hangs without this
	try:
		
		url = 'http://www.facebook.com/login.php'
		soup = authenticate(browser, url, args[0], args[1])	#Parses the html and stores in 'soup'
		fr_num_box = soup.find('span',attrs={'id':'requestsCountValue'})		#Finds span tags with the given ID
		info = "You have %s new friend requests\n" %(fr_num_box.text)		#Displays and gives the string between the span tags (<span>...</span>)

		msg_num_box = soup.find('span',attrs={'id':'mercurymessagesCountValue'})
		info +="You have %s unread messages\n" %(msg_num_box.text)

		notifs_num_box = soup.find('span',attrs={'id':'notificationsCountValue'})
		info += "You have %s unread notifications"%(str(int(notifs_num_box.text)+1))

		bot.sendChatAction(chat_id = update.message.chat_id, action = ChatAction.TYPING)
		bot.sendMessage(chat_id = update.message.chat_id, parse_mode=ParseMode.HTML, text = info)

	except AttributeError:
		error = "Either the password or email id you've entered is wrong"
		bot.sendChatAction(chat_id = update.message.chat_id, action = ChatAction.TYPING)
		bot.sendMessage(chat_id = update.message.chat_id, text = error)



def news(bot, update):
	bot.sendChatAction(chat_id = update.message.chat_id, action = ChatAction.TYPING)
	url='https://in.reuters.com/news/top-news'
	bulletins = ""
        r=requests.get(url) # The very old get function
        soup=BeautifulSoup(r.content,'html.parser') #Getting content
        links=soup.find_all(href=re.compile('/article/')) #getting every link which has the word article
        for i in links:
		if(i.text != 'Continue Reading'):
			if(i.text != "" ):
                		bulletins +="->" + i.text + '\n' #printing out text of the blockquote
	bot.sendMessage(chat_id = update.message.chat_id, parse_mode=ParseMode.HTML, text = bulletins)



def lyrics(bot,update,args):
	try:
		s=requests.Session() 			#It is having so many redirects so use of session is helpful or we get an error
		s.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36' #Headers
		r=s.get(get_url(args)) 			#Session get similarl to requests.get()
		soup=BeautifulSoup(r.content,'html.parser')
		temp=str(soup.findAll(class_='row'))
		temp=temp.replace('\\n','')
		temp=temp.split('<br/>') 		#Modifications of source code to get our required outcome
		lyrics = temp[2].split('\\r')[-1]
		for i in temp:				#Loop is for modifying each string so that no junk appears except \n
			if '<' in i:
		    		pass
			else:
		    		lyrics+=i + '\n'	#adding a new line character for easy reading purposes

		bot.sendChatAction(chat_id = update.message.chat_id, action = ChatAction.TYPING)
		bot.sendMessage(chat_id = update.message.chat_id, parse_mode=ParseMode.HTML, text = lyrics)

	except IndexError:
		error = "Can't find the song you asked for, please try another song"
		bot.sendChatAction(chat_id = update.message.chat_id, action = ChatAction.TYPING)
		bot.sendMessage(chat_id = update.message.chat_id, parse_mode=ParseMode.HTML, text = error)
	except UnboundLocalError:
		error = "Can't find the song you asked for, please try another song"
		bot.sendChatAction(chat_id = update.message.chat_id, action = ChatAction.TYPING)
		bot.sendMessage(chat_id = update.message.chat_id, parse_mode=ParseMode.HTML, text = error)
	


def wiki(bot, update, args):
	try:
		topic = ""
		for arg in args:
			topic += arg + " "
		summary = wikipedia.summary(topic, sentences = 30)
		page = wikipedia.page(topic)
		extra = "\nFor more details visit " + page.url
		summary += extra
		bot.sendChatAction(chat_id = update.message.chat_id, action = ChatAction.TYPING)
		bot.sendMessage(chat_id = update.message.chat_id, parse_mode=ParseMode.HTML, text = summary)

	except wikipedia.exceptions.DisambiguationError as e:
		error = "Please be more specific with your search query as there are a couple of other options meaning the same."
		for options in e.options:
			error += options.decode("utf-8","ignore")+'\n'
		bot.sendChatAction(chat_id = update.message.chat_id, action = ChatAction.TYPING)
		bot.sendMessage(chat_id = update.message.chat_id, text = error)

	except wikipedia.exceptions.PageError:
		error = "No messages could be found with the topic you entered!"
		bot.sendChatAction(chat_id = update.message.chat_id, action = ChatAction.TYPING)
		bot.sendMessage(chat_id = update.message.chat_id, text = error)


def help(bot, update):
	bot.sendChatAction(chat_id = update.message.chat_id, action = ChatAction.TYPING)
	bot.sendMessage(chat_id = update.message.chat_id, text = '''
		The following are the avaiable commands with me!\n
		/news				To get news bulletins
		/lyrics <name_of_song>		To get lyrics of songs
		/wiki <topic>			To get wikipedia summary on a given topic
		/fb <username> <password>	To get certain facebook updates
	''')



if __name__=='__main__':
	TOKEN = '482353144:AAHEfKVF_ibk2gAMI3T7sSk37u2ZU8P3PKQ'
	PORT = int(os.environ.get('PORT', '8443'))


	updater = Updater(TOKEN)

	updater = Updater(token=TOKEN)
	
	dispatcher = updater.dispatcher

	dispatcher.add_handler(CommandHandler('start',start))

	dispatcher.add_handler(CommandHandler('help',help))

	dispatcher.add_handler(CommandHandler('news',news))

	dispatcher.add_handler(CommandHandler('lyrics',lyrics,pass_args = True))

	dispatcher.add_handler(CommandHandler('wiki',wiki,pass_args = True))
	
	dispatcher.add_handler(CommandHandler('fb',fb,pass_args = True))
	
	updater.start_polling()
