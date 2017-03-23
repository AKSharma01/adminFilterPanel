from test.models import Postgres
from tasks import *
from users import *
# from tasksFilters import *
from taskTransformer import *

_table = {
		"task" : "tasks",
		"user" : "users",
		"style" : "styles",
		"customer" : "customers",
		"line" : "lines",
		"tna" : "tna_items",
		"taskStatus" : "task_status",
		"taskAssinee" : "tasks_assignees"
	}


def getTable(app):
	return _table[app]



def getByTableName(table, request_in_dict):
	if table == 'tasks':

		if len(request_in_dict) == 1 and request_in_dict['page']:
			data = function(page=request_in_dict['page'])
		else:
			data = paramRequest(request_in_dict)
		return data

