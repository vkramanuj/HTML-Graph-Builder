#! /usr/bin/python
# webcrawler and spider.add, a*
import urllib
from lxml import etree

def get_source(link):
	try:
		webPage = urllib.urlopen(link)
		source = webPage.read()
		webPage.close()
		return source
	except Exception, e:
		return "NOTHING"

class HTMLObject:
	"""docstring for HTMLObject"""
	def __init__(self, link):
		self.link = link
		self.source = "null"

	def get_source(self):
		if self.source == "null":
			self.source = get_source(link)

		return self.source

	
def parse_with_tree(source):
	print source 
so = get_source("https://docs.python.org/2/tutorial/inputoutput.html")
parse_with_tree(so)