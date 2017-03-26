from test.models import *

class Techpacks:
	def __init__(self):
		self.postgres = Postgres()

	def bindWithColumn(self,data,columns):
		data_dict = {}
		for idx,column in enumerate(columns):
			# if column[0] not in data_dict:
			data_dict[column[0]] = data[idx]
		return data_dict

	def getTechpack(self, techpack_id, page=0):
		techpack_dict = {
			'column_name' : 'id',
			'column_value' : techpack_id
		}
		if len(techpack_dict.keys()) :
			techpacks,columns = self.postgres.getByAppName('techpacks2',techpack_dict)
		else:
			techpacks,columns = self.postgres.getByAppName('techpacks2',page= page)
		techpack_data = []
		for techpack in techpacks:
			data = self.bindWithColumn(techpack, columns)		
			techpack_data.append(data)
		return techpack_data



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
