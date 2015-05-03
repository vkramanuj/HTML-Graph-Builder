from HTMLGraph import HTMLNode
from HTMLObject import HTMLObject
start = HTMLNode(HTMLObject("http://www.tweepy.org"), 1)
start.populate_graph()

start.print_node()