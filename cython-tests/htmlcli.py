#! /usr/local/bin/python
# webcrawler and spider.add, a* algos
# Command line interface for HTMLObject, reads from standardin

from HTMLObject import HTMLObject
from sys import stdin, stdout

args = stdin.readline()

html = HTMLObject(args)
links = html.get_links()
args = args[:-1]

for a, b, link, d in links:
	if link[0:4] == "http":
		print link
	else:
		print args + link