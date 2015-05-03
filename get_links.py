#! /usr/bin/python
# webcrawler and spider.add, a*
import urllib
import HTMLObject
from lxml import etree

def get_source(link):
	try:
		webPage = urllib.urlopen(link)
		source = webPage.read()
		webPage.close()
		return source
	except Exception, e:
		return "NOTHING"
	
def parse_with_tree(source):
	print source 
so = get_source("https://docs.python.org/2/tutorial/inputoutput.html")
parse_with_tree(so)