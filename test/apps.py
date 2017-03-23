from db.tables import *
from flask import request

class App:

	def __init__(self, app):
		self.table = getTable(app)
		print self.table

	def app(self):
		if request.args:
			request_in_dict = {}
			for key in request.args:
				request_in_dict[key] = request.args.get(key)
			
			data  = getByTableName(self.table, request_in_dict)
		else:
			data = getTableData(self.table)
		
		return data