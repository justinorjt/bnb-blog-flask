from marshmallow import Schema, fields

class googleArticle():
	"""google article fields"""
	def __init__(self, arg):
		super(googleArticle, self).__init__()
		self.arg = arg
		