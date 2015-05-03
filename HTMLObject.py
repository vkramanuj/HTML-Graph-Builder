class HTMLObject:
	"""docstring for HTMLObject"""
	def __init__(self, link):
		self.link = link
		self.source = "null"

	def get_source(self):
		if self.source == "null":
			self.source = get_source(link)

		return self.source