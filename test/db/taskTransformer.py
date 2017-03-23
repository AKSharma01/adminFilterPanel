from tasks import *
from ChangeParamNameWithColumnName import taskTable

def paramRequest(param_request):
	page = param_request['page'] if param_request['page'] else 0
	tasks_filters = TasksFilters(page)
	print param_request
	list_task_id = []
	for param in param_request:
		if "creator" == param:
			creator_task_id = tasks_filters.getCreatorTaskId(param_request[param])
			list_task_id.append(creator_task_id)
			# print creator_task_id

		elif "assignee" == param:
			assignee_task_id = tasks_filters.getAssigneeTaskId(param_request[param])
			list_task_id.append(assignee_task_id)

		elif "follower" == param:
			follower_task_id = tasks_filters.getFollowerTaskId(param_request[param])
			list_task_id.append(follower_task_id)

		elif "dueDate" == param:
			dueDate_task_id = tasks_filters.getDueDateTaskId(param_request[param])
			list_task_id.append(dueDate_task_id)
		elif "status" == param:
			data_task_id = tasks_filters.getDataStatusId(param_request[param])
			list_task_id.append(data_task_id)
		
		elif "page" != param:
			data_task_id = tasks_filters.getDataTaskId(param_request[param], param)
			list_task_id.append(data_task_id)



	offset = int(page)*10
	limit = 10


	task_ids = []
	common_task_id = []
	if list_task_id[0] is not None:
		common_task_id = list_task_id[0]
		for s in list_task_id:
			common_task_id = common_task_id & s
		common_task_id = list(common_task_id)
		length = len(common_task_id)
		for idx in range(offset, length):
			if idx-limit is offset :
				break
			s = common_task_id[idx]
			task_ids.append(s)
		print len(task_ids)
		print length

	return function(task_ids)
	# return function(common_task_id, param_request['page'] if param_request['page'] else 0)


class TasksFilters:
	"""docstring for TasksFilters"""
	def __init__(self, page):
		self.task = Tasks()
		self.page = page

	def getListUserId(self, users):
		users = users.split(' ')
		user_email = []
		for user in users:
			user_email.append(user)
		user_dict = {
			'column_to_get' : 'id',
			'table_name' : 'users',
			'column_name' : 'email',
			'column_value' : user_email
		}
		return self.task.getTableId(user_dict)


	def getSetObject(self, list_tuple_task_id):
		seen = set()
		for s in list_tuple_task_id:
			for x in s:
				if x not in seen:
					seen.add(x)
		return seen

	def getCreatorTaskId(self, creators):
		list_user_id = self.getListUserId(creators)
		user_dict = {
			'column_to_get' : 'id',
			'table_name' : 'tasks',
			'column_name' : 'creator_id',
			'column_value' : list_user_id,  #  list of immutable list 
			# 'page' : self.page
		}
		return self.getSetObject(self.task.getTableId(user_dict))


	def getAssigneeTaskId(self, assignees):
		list_user_id = self.getListUserId(assignees)
		user_dict = {
			'column_to_get' : 'task_id',
			'table_name' : 'tasks_assignees',
			'column_name' : 'assignee_id',
			'column_value' : list_user_id,
			# 'page' : self.page
		}
		return self.getSetObject(self.task.getTableId(user_dict))


	def getFollowerTaskId(self, followers):
		list_user_id = self.getListUserId(followers)
		user_dict = {
			'column_to_get' : 'task_id',
			'table_name' : 'task_followers',
			'column_name' : 'follower_id',
			'column_value' : list_user_id,
			# 'page' : self.page
		}
		return self.getSetObject(self.task.getTableId(user_dict))


	def getDueDateTaskId(self, dueDate):
		dueDate = dueDate.split(' ')
		due_date_dict = {
			'column_to_get' : 'id',
			'table_name' : 'tasks',
			'column_name' : 'due_date',
			'column_value' : dueDate,
			# 'page' : self.page
		}
		return self.getSetObject(self.task.getTableIdByDueDate(due_date_dict))
		# print list_tuple_task_id
		# print "******"*20
		# print "******"*20
	
	def getDataTaskId(self, data, param):
		data = data.split(' ')
		data_dict = {
			'column_to_get' : 'id',
			'table_name' : 'tasks',
			'column_name' : taskTable[param],
			'column_value' : data
		}
		return self.getSetObject(self.task.getTableId(data_dict))

	def getDataStatusId(self, data):
		make_list = []
		make_list.append(data)
		data_dict = {
			'column_to_get' : 'id',
			'table_name' : 'task_status',
			'column_name' : 'status',
			'column_value' : make_list
		}
		data = self.task.getTableId(data_dict)
		data_dict = {
			'column_to_get' : 'id',
			'table_name' : 'tasks',
			'column_name' : 'status_id',
			'column_value' : data[0]
		}
		data = self.task.getTableId(data_dict)
		return self.getSetObject(data)