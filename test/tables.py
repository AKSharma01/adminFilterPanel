from test.models import Postgres
from tasks.tasks import *
from tasks.tasks import *

_table = {
		"task" : "tasks",
		"user" : "users",
		"style" : "styles",
		"customer" : "customers",
		"line" : "lines",
		"techpack" : "techpacks2"
	}


def getTable(app):
	return _table[app]

























# def getByTableName(table, request_in_dict={}):
# 	# if table == 'tasks':
# 	# 	data = paramRequest(request_in_dict)
# 	# return data
# 	module_name = getTable(table)
# 	module = importlib.import_module('test.'+module_name+'.'+module_name)
# 	print module
# 	data = module.paramRequest(request_in_dict)
# 	return data