from tasks import *

def paramRequest(param_request):
	tasks_filters = TasksFilters(param_request)
	print param_request
	# only takes the tasks ids for every request and at the end interset the ids 
	# to get the common filter task id then and there we could process further for 
	# task reslationship to get the whole data

	if "creator" in param_request:
		data = tasks_filters.getTaskIdByCreator(param_request['creator'])
	if "assignee" in param_request:
		data = tasks_filters.getTaskIdByAssignee(param_request['assignee'])
	if "follower" in param_request:
		data = tasks_filters.getTaskIdByFollower(param_request['follower'])
	if "dueDate" in param_request:
		data = tasks_filters.getTaskIdByDueDate(param_request['dueDate'])
	
	return data

class TasksFilters:
	"""docstring for TasksFilters"""
	def __init__(self, param_request):
		self.param_request = param_request
		self.task = Tasks()
#================================ correct data but wrong idea =======================	
# ||	def getTaskIdByCreator(self, creator):										||
# ||		creator_dict = {														||
# ||			'column_name' : 'email',											||
# ||			'column_value' : creator 											||
# ||		}																		||
# ||		creator_dict = self.task.getUser(creator_dict)							||
# ||		creator_id = creator_dict['id']											||
# ||		return function(creator_id=creator_id)									||
#=====================================================================================
	
	def getTaskIdByCreator(self, creator):
		creator_list = creator.split(' ')
		creator_list_data = []
		for creator in creator_list:
			creator_dict = {
				'column_name' : 'email',
				'column_value' : creator
			}
			creator_dict = self.task.getUser(creator_dict)
			task_dict = {
				'column_name' : 'creator_id',
				'column_value' : creator_dict['id']
			}
			return function(task_dict=task_dict)
			creator_list_data.append(function(task_dict=task_dict))
		return creator_list_data

	def getTaskIdByAssignee(self, assignee):
		user_dict = {
			'column_name' : 'email',
			'column_value' : assignee
		}
		user = self.task.getUser(user_dict)
		assignee_dict = {
			'column_name' : 'assignee_id',
			'column_value' : user['id']
		}
		assignee_list_dict,assignee_task_id_list = self.task.getAssignee(assignee_dict)
		assignee_list = []
		for assignee_task_id in assignee_task_id_list:
			assignee_task_id = {
				'column_name' : 'id',
				'column_value' : assignee_task_id
			}
			assignee_list.append(function(assignee_task_id)[0])

		return assignee_list



	def getTaskIdByFollower(self,follower):
		user_dict = {
			'column_name' : 'email',
			'column_value' : follower
		}
		user = self.task.getUser(user_dict)
		follower_dict = {
			'column_name' : 'follower_id',
			'column_value' : user['id']
		}
		follower_list_dict, follower_task_id_list = self.task.getFollower(follower_dict)
		follower_list = []
		for follower_task_id in follower_task_id_list:
			follower_task_id = {
				'column_name' : 'id',
				'column_value' : follower_task_id
			}
			follower_list.append(function(follower_task_id)[0])
		return follower_list

	def getTaskIdByDueDate(self, dueDate):
		dueDate = dueDate.split(' ')
		dueDate_dict = {
			'column_name' : 'due_date',
			'column_value' : dueDate
		}
		task_id_list = self.task.getTask(dueDate_dict)
		id_list = []
		for task_id in task_id_list:
			# print task_id['id']
			dueDate_dict = {
				'column_name' : 'id',
				'column_value' : task_id['id']
			}
			id_list.append(function(dueDate_dict)[0])
		return id_list


