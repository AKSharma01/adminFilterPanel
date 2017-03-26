from tables import *
from flask import request
import importlib

class App:

	def __init__(self, app):
		self.table = getTable(app)
		print self.table

	def app(self):
		if request.args:
			request_in_dict = {}
			for key in request.args:
				request_in_dict[key] = request.args.get(key)
			module = importlib.import_module('test.'+self.table+'.'+self.table)
			print module
			data = module.paramRequest(request_in_dict)
			return data
			
			
