# TestFile
from __future__ import print_function
from HTMLObject import HTMLObject

html = HTMLObject("http://lxml.de/lxmlhtml.html#working-with-links")
links = html.get_links()
print(html.get_links())