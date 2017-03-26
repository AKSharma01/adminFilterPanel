from test.models import *
from tasksRepository import Tasks
import json
""" This 'task' variable contain the column name which we want to display """

taskClass = Tasks()

def getData(table_name, column_name, column_value):
	return taskClass.getCLS({
		"table_name" : table_name,
		"column_name" : column_name,
		"column_value" : column_value
	})

def getPS(table_name, column_name, column_value):
	return taskClass.getPSData({
		"table_name" : table_name,
		"column_name" : column_name,
		"column_value" : column_value
	})




def function(task_list=[], page=0):

	task_data_list = []
	for taskid in task_list:
		task = taskClass.getTask(task_id = taskid, page = page)[0]

		# ===================== passing dict for creator ==============
		dict1 = {
			'column_name' : 'id',
			'column_value' : task['creator_id']
		}
		creator = taskClass.getUser(dict1)

		#====================== passing dict for assignee ==============
		dict1 = {
			'column_name' : 'task_id',
			'column_value' : task['id']
		}
		assignees, assignees_task_id_list = taskClass.getAssignee(dict1)
		#====================== passing dict for follower ==============
		dict1 = {
			'column_name' : 'task_id',
			'column_value' : task['id']
		}
		followers, followers_task_id_list = taskClass.getFollower(dict1)
		data = {
			'id' : task['id'],
			'title' : task['title'],
			# 'description' : task['description'],
			'dueDate' : task['due_date'],
			# 'seen' : task['seen'],
			'isSubmitted' : task['is_submitted'],
			'isCompleted' : task['is_completed'],
			# 'completionDate' : task['completion_date'],
			# 'location' : json.loads(task['location']) if type(task['location']) is str else task['location'],
			# 'status' : task['status'],
			# 'deletedAt' : task['deleted_at'],
			# 'createdAt' : task['created_at'],
			# 'updatedAt' : task['updated_at'], #toDateTimeString(),
			# 'submissionDate' : task['submission_date'],
			# 'tnaItemId' : task['tnaItem'],
			# 'archivedAt' : task['archived_at'],
			# 'needApproval' : task['need_approval'],
			# 'isApproved': task['is_approved'],
			'schemaVersion': task['schema_version'],
			'isAssignee' : True if assignees else False,
			'assignee' : assignees,
			# 'isflagged' : False if userFlagged else userFlagged['is_enabled'],
			'isFollower' : True if followers else False ,
			'creator' : creator,
			'followers' : followers,
			'status' : getPS('task_status', 'id', task['status_id']),
			'line' : getData('lines', 'id', task['line_id']) if task['line_id'] else None,
			'style' : getData('styles', 'id', task['style_id']) if task['style_id'] else None,
			'customer' : getData('customers', 'id', task['customer_id']) if task['customer_id'] else None,
			# 'notes' : taskStatusNote['data'],
			# 'attachments' : attachments['data'],
			# 'priority' : getPS('priorities'),
			# 'comments' : comments['data'],
			# 'categories' : categories['data'],
			# 'tags' : tags['data'],
			# 'isMilestone' : isMilestone,
			# 'dependentItems' : dependentItems,
			# 'tna' : tna,
			# 'materialRequest': taskMaterial,
			# 'reminder' : reminder,
			# 'type' : TaskHelper::checkType($task),
			# 'nextStatus': this.nextStatus(task),
			# 'tabStatus' : this.getTabStatus(task),
			# 'checklist' : isset($task->checklist) ? json_decode($task->checklist) : [],
			# 'assigneeStatus' : $task->assigneeStatuses->status,
			# 'snoozedTime' : $task->snoozedTime,
			# 'startedBy' : isset($starter) ? $starter : NULL,
			# 'submittedBy' : isset($submitter) ? $submitter : NULL,
		}
		task_data_list.append(data)
	return task_data_list



























































	# def check(self, request_in_dict):
	# 	for key in request_in_dict:
	# 		if task[key] in taskRelationShip and task[key]=='creator_id':
	# 			dict_id = {}
	# 			users_link = taskRelationShip[task[key]]
	# 			id = self.postgres.getByUser(request_in_dict[key])
	# 			dict_id['creator_id'] = id[0]
	# 			task_data = self.postgres.fetchDetailsWithoutJoin('tasks', dict_id)
				
	# 			return task_data
	# 		if key == "assignee":
	# 			dict_id = {}
	# 			users_link = taskRelationShip[task[key]]
	# 			user_id = self.postgres.getByUser(request_in_dict[key])
	# 			print user_id
	# 			task_id = self.postgres.getByAssignee(user_id[0][0])
	# 			print task_id
	# 			task_list = []
	# 			for id in task_id: 
	# 				print id[0]
	# 				dict_id['id'] = id[0]
	# 				task_data = self.postgres.fetchDetailsWithoutJoin('tasks', dict_id)
	# 				task_list.append(task_data)
	# 			return task_list







# def checkRelationShip(self,key):
# 	if task[key] in taskRelationShip:
# 		dict_relation = {}
# 		relation = taskRelationShip[task[key]]
# 		for key in relation:
# 			if key == 'table_name':
# 				tablename = relation[key]
# 			else:
# 				dict_relation[key] = relation[key]
# 		data = Postgres().fetchDetailsWithoutJoin(tablename, dict_relation)
# 		print data




























# task = {
# 	"id":"id",
# 	"title":"title",
# 	"description":"description",
# 	"creatorId":"creator_id",
# 	"isAssigneeGroup":"is_assignee_group",
# 	"dueDate":"due_date",
# 	"seen":"seen",
# 	"isSubmitted":"is_submitted",
# 	"isCompleted":"is_completed",
# 	"submissionDate":"submission_date",
# 	"completionDate":"completion_date",
# 	"priorityId":"priority_id",
# 	"location":"location",
# 	"statusId":"status_id",
# 	"deletedAt":"deleted_at",
# 	"createdAt":"created_at",
# 	"updatedAt":"updated_at",
# 	"tnaItemId":"tna_item_id",
# 	"archivedAt":"archived_at",
# 	"createdFrom":"created_from",
# 	"createdFromId" : "created_from_id",
# 	"googleCalendarId":"google_calendar_id",
# 	"checklist":"checklist",
# 	"lineId":"line_id",
# 	"styleId":"style_id",
# 	"customerId":"customer_id",
# 	"needApproval":"need_approval",
# 	"isApproved":"is_approved",
# 	"starterId":"starter_id",
# 	"submitterId":"submitter_id",
# 	"schemaVersion":"schema_version",
# 	"assignee" : "assignee"
# }


# def function1(dict_data):
# 	return {
# 		'id' : dict_data['id'],
# 		'userId' : dict_data['creator_id'],
# 		'title' : dict_data['title'],
# 		'description' : dict_data['description'],
# 		'dueDate' : dict_data['due_date'],
# 		'seen' : dict_data['seen'],
# 		'isSubmitted' : dict_data['is_submitted'],
# 		'isCompleted' : dict_data['is_completed'],
# 		'completionDate' : dict_data['completion_date'],
# 		'location' : json.loads(dict_data['location']) if (type(dict_data['location']) is str) else dict_data['location'],
# 		# 'status' : dict_data['status'],
# 		'deletedAt' : dict_data['deleted_at'],
# 		'createdAt' : dict_data['created_at'],
# 		'updatedAt' : dict_data['updated_at'], #toDateTimeString(),
# 		'submissionDate' : dict_data['submission_date'],
# 		# 'tnaItemId' : dict_data['tna_item'],
# 		'archivedAt' : dict_data['archived_at'],
# 		'needApproval' : dict_data['need_approval'],
# 		'isApproved': dict_data['is_approved'],
# 		'schemaVersion': dict_data['schema_version']

# 	}







# taskRelationShip = {
# 	"creator" : {
# 		'table_name': 'users',
# 		'column_name':'email'
# 	},
# 	"status" : {
# 		'table_name' : 'tasks_status',
# 		'column_name' : 'id'
# 	},
# 	"tna" : {
# 		'table_name' : 'tna_items',
# 		'column_name' : 'id'
# 	},
# 	"line" : {
# 		'table_name' : 'lines',
# 		'column_name' : 'id'
# 	},
# 	"style" : {
# 		'table_name':'styles',
# 		'column_name' : 'id'
# 	},
# 	"customer" : {
# 		'table_name':'customers',
# 		'column_name' : 'id'
# 	},
# 	"assignee" : {
# 		"table_name" : "tasks_assaignee",
# 		"column_name" : "id",
# 		"foreign_table" : {
# 			"table_name" : "users",
# 			"column_name" : "email",
# 			"find_column" : "id"
# 		}
# 	}
# }
