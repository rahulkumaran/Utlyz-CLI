from setuptools import setup

setup(
	name='utlyz',
	version=1.0,
	py_modules=[
		'fbcli',
		'cricbuzz',
		'lyrics',
	],
	install_requires=[
		'click',
		'bs4',
		'BeautifulSoup',
		'mechanize',
		'requests',
	],
	entry_points={
		'console_scripts':[
		'fbcli=fbcli:cli',
		'cricbuzz=cricbuzz:cli',
		'lyrics=lyrics:cli',
		]
	},
)
