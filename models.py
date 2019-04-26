from marshmallow import Schema, fields

# class googleArticle():
# 	"""google article fields"""
# 	def __init__(self, arg):
# 		super(googleArticle, self).__init__()
# 		self.arg = arg
		
class BlogPost(Schema):
  id = fields.Int(required=True)
  repo_name = fields.Str()
  full_name = fields.Str()
  description = fields.Str()
