from lxml.html import iterlinks
import sys
import urllib
class HTMLObject(object):
	"""HTMLObject manages html links, does lazy initialization for everything"""
	def __init__(self, link):
		self.link = link
		self.source = "null"
		self.links = []
		self.parsed = []

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

	def parsed_links(self):
		if self.parsed == []:
			self.parsed = [(link if link[0:4] == "http" else self.link + link) for a, b, link, d in self.get_links()]
		
		return self.parsed

	def update(self, link = None):
		if link is None:
			link = self.link
		
		self.link = link
		self.source = "null"
		self.links = []
		self.parsed = []
		self.get_source(True)
		self.get_links(True)
		self.parsed_links()

	def link(self):
		return self.link