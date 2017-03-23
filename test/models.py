import psycopg2, psycopg2.extras
import env

class ENVSetting:
	"""docstring for ENVSetting"""
	def __init__(self):
		# self.username = self.password = self.database = self.host = ''
		pass

	def getPsqlENV(self):
		""" This will return the postgres access credential """
		username = getattr(env, env.ENV+'_username')
		password = getattr(env, env.ENV+'_password')
		database = getattr(env, env.ENV+'_database')
		host = getattr(env, env.ENV+'_host')
		return database, username, password, host
		
class Postgres:
	"""docstring for Postgres"""
	def __init__(self):
		db = "dbname=%s user=%s password=%s host=%s"%ENVSetting().getPsqlENV()
		# print db
		self.con = psycopg2.connect(db)
		self.cur = self.con.cursor()


	def getIdFormAnyTable(self, dict1):
		# page = int(dict1['page']) if 'page' in dict1 else 0
		query = "select {get_column} from {table_name} where ".format(get_column = dict1['column_to_get'], table_name = dict1['table_name'])
		for idx,column_value in enumerate(dict1['column_value']):
			if idx > 0:
				query = query + " or "
			if type(column_value) is tuple:
				column_value = column_value[0]
			query = query+" {column_name} = \'{column_value}\'".format(column_name=dict1['column_name'], column_value = column_value)
		# query = query + " limit 10 offset {offset}".format(offset = page*10)
		self.cur.execute(query)
		fetch_data = self.cur.fetchall()

		# print fetch_data, "&&&&&&&&&&&&&&&&&&&&&&&&", len(fetch_data)
		return fetch_data


	def getIdFromTaskTableByDueDate(self, dict1, page=0):
		query = "select {get_column} from {table_name} where {column_name} between \'{from_due_date}\' and \'{to_due_date}\'  "\
		.format(get_column = dict1['column_to_get'], table_name = dict1['table_name'], column_name = dict1['column_name'], \
		from_due_date = dict1['column_value'][0], to_due_date = dict1['column_value'][1]) 
		self.cur.execute(query)
		return self.cur.fetchall()

	def getPSFromTable(self, dict1):
		query = "select * from {0} where {1} = {2}".format(dict1['table_name'], dict1['column_name'], dict1['column_value'])
		self.cur.execute(query)
		return self.cur.fetchall()

	def getByAppName(self, tablename, dict1=None, page=0):
		if dict1 == None:
			offset = int(page)*10
			query = """ SELECT * FROM {tablename} limit 10 offset {offset}""".format(tablename = tablename, offset = offset)
		elif len(dict1['column_value'])==2 :
			query = """ SELECT * FROM {tablename} WHERE {column_name} BETWEEN \'{fromDueDate}\' AND \'{toDueDate}\' limit 10""".format(tablename = tablename, column_name = dict1['column_name'], fromDueDate = dict1['column_value'][0], toDueDate = dict1['column_value'][1])
		else :
			query = """ SELECT * FROM {tablename} where {column_name} = \'{column_value}\' """.format(tablename = tablename, column_name = dict1['column_name'], column_value = dict1['column_value'] )
		self.cur.execute(query)
		return self.cur.fetchall(), self.getTableColumn(tablename)



	def fetchDetailsWithoutJoin(self, tableName, params=None):
		cursor = self.con.cursor(cursor_factory=psycopg2.extras.DictCursor)
		fields = ', '.join(params.keys())
		values = ', '.join(['%%(%s)s' % x for x in params])
		if params:
			query = 'SELECT * FROM %s WHERE (%s)=(%s)' %(tableName, fields, values)
		else:
			query = 'SELECT * FROM %s ' %(tableName)
		cursor.execute(query, params)
		self.con.commit()
		return self.bindColumnNameWithData(cursor.fetchall())

	def bindColumnNameWithData(self,  data):
		result = []
		if len(data) == 1:
			return dict(data[0])
		for row in data:
			result.append(dict(row))
		return result



	def getTableColumn(self, tablename):
		""" this method will return the column name of the table """
		query = "SELECT column_name FROM information_schema.columns WHERE table_schema='public' AND table_name=\'{tablename}\'".format(tablename = tablename)
		self.cur.execute(query)
		return self.cur.fetchall()


	# def get(self, toFind='*', tablename):
	# 	query = "SELECT "
	# 	pass

	# def where(self, dictToSearch):
	# 	pass

	# def date(self, date):
	# 	pass

	# def paginate(self, length):
	# 	pass

