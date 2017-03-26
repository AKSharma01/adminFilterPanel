from test.models import *

class Tasks:
	def __init__(self):
		self.postgres = Postgres()

	def bindWithColumn(self,data,columns):
		data_dict = {}
		for idx,column in enumerate(columns):
			data_dict[column[0]] = data[idx]
		return data_dict

	def getTask(self, task_id, page=0):
		"""
		=================================================================================
			Check this first if multiple task is coming. this could contain the error.
		=================================================================================
		"""
		task_dict = {
			'column_name' : 'id',
			'column_value' : task_id
		}
		if len(task_dict.keys()) :	
			tasks,columns = self.postgres.getByAppName('tasks',task_dict)
		else:
			tasks,columns = self.postgres.getByAppName('tasks',page= page)
		task_data = []
		for task in tasks:
			data = self.bindWithColumn(task, columns)
			task_data.append(data)
		return task_data

	def getUser(self, dict1):
		
		creator, columns = self.postgres.getByAppName('users',dict1)
		# print creator, columns
		data = self.bindWithColumn(creator[0], columns)
		dict_creator={}
		dict_creator['id'] = data['id']
		dict_creator['displayName'] = data['display_name']
		dict_creator['email'] = data['email']
		dict_creator['logo'] = data['logo']
		return dict_creator

	def getAssignee(self, dict1):
		# print task_id		
		assignees, columns = self.postgres.getByAppName('tasks_assignees',dict1)
		assignee_list = []
		assignee_task_id_list = []
		for assignee in assignees:
			data = self.bindWithColumn(assignee, columns)
			# print data
			assignee_task_id_list.append(data['task_id'])
			dict1 = {
				'column_name' : 'id',
				'column_value' : data['assignee_id']
			}
			dict_assignee = self.getUser(dict1)
			assignee_list.append(dict_assignee)
		return assignee_list,assignee_task_id_list


	def getFollower(self, dict1):
		followers, columns = self.postgres.getByAppName('task_followers',dict1)
		follower_list = []
		follower_task_id_list = []
		for follower in followers:
			data = self.bindWithColumn(follower, columns)
			follower_task_id_list.append(data['task_id'])
			dict1 = {
				'column_name' : 'id',
				'column_value' : data['follower_id']
			}
			dict_follower = self.getUser(dict1)
			follower_list.append(dict_follower)
		return follower_list, follower_task_id_list

	
	def getCLS(self, dict1):
		clss, columns = self.postgres.getByAppName(dict1['table_name'],dict1)
		clss = clss[0]
		data = self.bindWithColumn(clss, columns)
		cls_dict = {
			"code" : data['code'],
			"name" : data['name'],
			"created_at" : data['created_at'],
			"updated_at" : data['updated_at']
		}
		return cls_dict



	def getPSData(self, dict1):
		ps = self.postgres.getPSFromTable(dict1)
		return ps[0][1]
		# data = self.bindWithColumn(ps, columns)
		# return data['status'] if data['status'] else data['priority']


	def getTableId(self, dict1):
		return self.postgres.getIdFormAnyTable(dict1)

	def getTableIdByDueDate(self, dict1):
		return self.postgres.getIdFromTaskTableByDueDate(dict1)


