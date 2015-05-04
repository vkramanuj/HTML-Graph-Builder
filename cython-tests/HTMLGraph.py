from HTMLObject import HTMLObject

class HTMLNode:
	"""HTMLNode from depth and object"""
	def __init__(self, obj, depth, from_link = ""):
		self.init_node = obj
		self.curr_link = obj.link
		self.graph = []
		self.depth = depth
		self.prev_link = from_link

	def populate_graph(self):
		for link in self.init_node.parsed_links():
			obj = HTMLObject(link)
			node = HTMLNode(obj, self.depth - 1, self.curr_link)

			if node.depth > 0:
				node.populate_graph()

			self.graph.append(node)

	def get_graph(self):
		if self.graph == []:
			self.populate_graph()

		return self.graph

	def print_node(self, precursor = ""):
		print precursor + self.curr_link

		for obj in self.graph:
			obj.print_node(precursor + "\t")

	def expand(self, dep):
		depth = dep
		self.populate_graph()