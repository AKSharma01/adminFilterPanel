from techpacksTransfomer import *
from ChangeParamNameWithColumnName import techpackTable, techpackForeignTable, techpackFilterByKey

def paramRequest(param_request):
	try:
		page = param_request['page']
		del param_request['page']
	except :
		page = 0
	techpacks_filters = TechpacksFilters(page)
	# print param_request
	list_techpack_id = []
	for param in param_request:
		if param in techpackFilterByKey:
			data_techpack_id = techpacks_filters.getDataTechpackId(param_request[param], param)
			list_techpack_id.append(data_techpack_id)


	offset = int(page)*10
	limit = 10
	techpack_ids = []
	if list_techpack_id:
		common_techpack_id = []
		common_techpack_id = list_techpack_id[0]
		for s in list_techpack_id:
			common_techpack_id = common_techpack_id & s
		common_techpack_id = list(common_techpack_id)
		length = len(common_techpack_id)
		for idx in xrange(offset, length):
			if idx-limit == offset :
				break
			s = common_techpack_id[idx]
			techpack_ids.append(s)
	# print len(techpack_ids)
	return function(techpack_ids)




class TechpacksFilters:
	"""docstring for TechpacksFilters"""
	def __init__(self, page):
		self.techpack = Techpacks()
		self.page = page



	def getSetObject(self, list_tuple_techpack_id):
		seen = set()
		for s in list_tuple_techpack_id:
			for x in s:
				if x not in seen:
					seen.add(x)
		return seen

	# def getCreatorTechpackId(self, creators):
	# 	list_user_id = self.getListUserId(creators)
	# 	user_dict = {
	# 		'column_to_get' : 'id',
	# 		'table_name' : 'techpacks',
	# 		'column_name' : 'creator_id',
	# 		'column_value' : list_user_id,  #  list of immutable list 
	# 		# 'page' : self.page
	# 	}
	# 	return self.getSetObject(self.techpack.getTableId(user_dict))



	def getDueDateTechpackId(self, dueDate):
		dueDate = dueDate.split(' ')
		due_date_dict = {
			'column_to_get' : 'id',
			'table_name' : 'techpacks',
			'column_name' : 'due_date',
			'column_value' : dueDate,
			# 'page' : self.page
		}
		return self.getSetObject(self.techpack.getTableIdByDueDate(due_date_dict))

	
	def getDataTechpackId(self, data, param):
		data = data.split(' ')
		data_dict = {
			'column_to_get' :  techpackForeignTable[techpackTable[param]]['column_name'] if techpackTable[param] in techpackForeignTable else "id",
			'table_name' : techpackForeignTable[techpackTable[param]]['table_name'] if techpackTable[param] in techpackForeignTable else "techpacks2",
			'column_name' : techpackForeignTable[techpackTable[param]]['column_to_find'] if techpackTable[param] in techpackForeignTable else techpackTable[param],
			'column_value' : data
		}
		if techpackTable[param] in techpackForeignTable:
			data_dict = {
				'column_to_get' : "id",
				'table_name' : "techpacks2",
				'column_name' : techpackTable[param],
				'column_value' : self.techpack.getTableId(data_dict)
			}

		return self.getSetObject(self.techpack.getTableId(data_dict))






	# def getListUserId(self, users):
	# 	users = users.split(' ')
	# 	user_email = []
	# 	for user in users:
	# 		user_email.append(user)
	# 	user_dict = {
	# 		'column_to_get' : 'id',
	# 		'table_name' : 'users',
	# 		'column_name' : 'email',
	# 		'column_value' : user_email
	# 	}
	# 	return self.techpack.getTableId(user_dict)

	# def getAssigneeTechpackId(self, assignees):
	# 	list_user_id = self.getListUserId(assignees)
	# 	user_dict = {
	# 		'column_to_get' : 'techpack_id',
	# 		'table_name' : 'techpacks_assignees',
	# 		'column_name' : 'assignee_id',
	# 		'column_value' : list_user_id,
	# 		# 'page' : self.page
	# 	}
	# 	return self.getSetObject(self.techpack.getTableId(user_dict))


	# def getFollowerTechpackId(self, followers):
	# 	list_user_id = self.getListUserId(followers)
	# 	user_dict = {
	# 		'column_to_get' : 'techpack_id',
	# 		'table_name' : 'techpack_followers',
	# 		'column_name' : 'follower_id',
	# 		'column_value' : list_user_id,
	# 		# 'page' : self.page
	# 	}
	# 	return self.getSetObject(self.techpack.getTableId(user_dict))