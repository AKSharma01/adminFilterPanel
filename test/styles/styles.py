from stylesTransfomer import *
from ChangeParamNameWithColumnName import styleTable, styleForeignTable, styleFilterByKey

def paramRequest(param_request):
	try:
		page = param_request['page']
		del param_request['page']
	except :
		page = 0
	styles_filters = StylesFilters(page)
	# print param_request
	list_style_id = []
	for param in param_request:
		if param in styleFilterByKey:
			data_style_id = styles_filters.getDataStyleId(param_request[param], param)
			list_style_id.append(data_style_id)
		elif "archived" in param:
			archive_style_id = styles_filters.getDueDateStyleId(param_request[param])
			list_style_id.append(archive_style_id)


	offset = int(page)*10
	limit = 10
	style_ids = []
	if list_style_id:
		common_style_id = []
		common_style_id = list_style_id[0]
		for s in list_style_id:
			common_style_id = common_style_id & s
		common_style_id = list(common_style_id)
		length = len(common_style_id)
		for idx in xrange(offset, length):
			if idx-limit == offset :
				break
			s = common_style_id[idx]
			style_ids.append(s)
	# print len(style_ids)
	return function(style_ids)




class StylesFilters:
	"""docstring for stylesFilters"""
	def __init__(self, page):
		self.style = Styles()
		self.page = page



	def getSetObject(self, list_tuple_style_id):
		seen = set()
		for s in list_tuple_style_id:
			for x in s:
				if x not in seen:
					seen.add(x)
		return seen

	def getDataStyleId(self, data, param):
		data = data.split(' ')

		data_dict = {
			'column_to_get' :  styleForeignTable[styleTable[param]]['column_name'] if styleTable[param] in styleForeignTable else "id",
			'table_name' : styleForeignTable[styleTable[param]]['table_name'] if styleTable[param] in styleForeignTable else "styles",
			'column_name' : styleForeignTable[styleTable[param]]['column_to_find'] if styleTable[param] in styleForeignTable else styleTable[param],
			'column_value' : data
		}
		print data_dict
		if styleTable[param] in styleForeignTable:
			data_dict = {
				'column_to_get' : "id",
				'table_name' : "styles",
				'column_name' : styleTable[param],
				'column_value' : self.style.getTableId(data_dict)
			}

		return self.getSetObject(self.style.getTableId(data_dict))



	def getDueDateStyleId(self, dueDate):
		dueDate = dueDate.split(' ')
		due_date_dict = {
			'column_to_get' : 'id',
			'table_name' : 'styles',
			'column_name' : "archived_at",
			'column_value' : dueDate,
			# 'page' : self.page
		}
		return self.getSetObject(self.style.getTableIdByDueDate(due_date_dict))

	




	# def getCreatorstyleId(self, creators):
	# 	list_user_id = self.getListUserId(creators)
	# 	user_dict = {
	# 		'column_to_get' : 'id',
	# 		'table_name' : 'styles',
	# 		'column_name' : 'creator_id',
	# 		'column_value' : list_user_id,  #  list of immutable list 
	# 		# 'page' : self.page
	# 	}
	# 	return self.getSetObject(self.style.getTableId(user_dict))


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
	# 	return self.style.getTableId(user_dict)

	# def getAssigneestyleId(self, assignees):
	# 	list_user_id = self.getListUserId(assignees)
	# 	user_dict = {
	# 		'column_to_get' : 'style_id',
	# 		'table_name' : 'styles_assignees',
	# 		'column_name' : 'assignee_id',
	# 		'column_value' : list_user_id,
	# 		# 'page' : self.page
	# 	}
	# 	return self.getSetObject(self.style.getTableId(user_dict))


	# def getFollowerstyleId(self, followers):
	# 	list_user_id = self.getListUserId(followers)
	# 	user_dict = {
	# 		'column_to_get' : 'style_id',
	# 		'table_name' : 'style_followers',
	# 		'column_name' : 'follower_id',
	# 		'column_value' : list_user_id,
	# 		# 'page' : self.page
	# 	}
	# 	return self.getSetObject(self.style.getTableId(user_dict))