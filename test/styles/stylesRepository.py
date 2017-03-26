from test.models import *

class Styles:
	def __init__(self):
		self.postgres = Postgres()

	def bindWithColumn(self,data,columns):
		data_dict = {}
		for idx,column in enumerate(columns):
			# if column[0] not in data_dict:
			data_dict[column[0]] = data[idx]
		return data_dict

	def getStyle(self, style_id, page=0):
		style_dict = {
			'column_name' : 'id',
			'column_value' : style_id
		}
		if len(style_dict.keys()) :
			styles,columns = self.postgres.getByAppName('styles',style_dict)
		else:
			styles,columns = self.postgres.getByAppName('styles',page= page)
		style_data = []
		for style in styles:
			data = self.bindWithColumn(style, columns)		
			style_data.append(data)
		return style_data



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
	
		

	def getTableId(self, dict1):
		return self.postgres.getIdFormAnyTable(dict1)

	def getTableIdByDueDate(self, dict1):
		return self.postgres.getIdFromTaskTableByDueDate(dict1)





	def getCLS(self, dict1):
		clss, columns = self.postgres.getByAppName(dict1['table_name'],dict1)
		clss = clss[0]
		data = self.bindWithColumn(clss, columns)
		print data
		cls_dict = {
			"code" : data['code'],
			"name" : data['name'],
			"created_at" : data['created_at'],
			"updated_at" : data['updated_at']
		}
		return cls_dict
