from lxml.html import iterlinks
import sys
import urllib
class HTMLObject(object):
	"""HTMLObject manages html links, does lazy initialization for everything"""
	def __init__(self, link):
		self.link = link
		self.source = "null"
		self.links = []

	def get_source(self, noReturn = False):
		if self.source == "null":
			source = ""
			try:
				webPage = urllib.urlopen(self.link)
				source = webPage.read()
				webPage.close()
			except Exception, e:
				source = "NOTHING"

			self.source = source

		if not noReturn:
			return self.source

	def get_links(self, noReturn = False):
		if self.links == []:
			so = self.get_source()
			self.links = list(iterlinks(so))
		
		if not noReturn:
			return self.links

	def update(self, link = None):
		if link is None:
			link = self.link
		
		self.link = link
		self.get_source(True)
		self.get_links(True)

	def link(self):
		return self.link