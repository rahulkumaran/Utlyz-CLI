from setuptools import setup

setup(
	name='fbcli',
	version=1.0,
	py_modules=['fbcli'],
	install_requires=[
		'click',
		'bs4',
		'BeautifulSoup',
		'mechanize',
	],
	entry_points='''
		[console_scripts]
		fbcli=fbcli:cli
		''',
)
