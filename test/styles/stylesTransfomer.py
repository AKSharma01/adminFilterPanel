from test.models import *
from stylesRepository import Styles
import json
from ChangeParamNameWithColumnName import styleForeignTable
""" This 'tstyle' variable contain the column name which we want to display """

styleClass = Styles()

def getCreator(column_value, dict):
	return styleClass.getUser({
		"table_name" : dict["table_name"],
		"column_name" : dict["column_name"],
		"column_value" : column_value
	})

def getCustomer(column_value, dict):
	return styleClass.getCLS({
		"table_name" : dict["table_name"],
		"column_name" : dict["column_name"],
		"column_value" : column_value
	})

def function(style_list=[], page=0):
	style_data_list = []
	for styleid in style_list:
		try:
			style = styleClass.getStyle(style_id = styleid, page = page)[0]
		except :
			continue
		data = {
				"id" : style["id"],
				"code" : style["code"],
				"name" : style["name"],
				# "line" : style["line_id"],
				# "tna" : style["tna_id"],
				# "techpack" : style["techpack_id"],
				# "order" : style["order_id"],
				"flat" : style["flat"],
				"deletedAt" : style["deleted_at"],
				"createdAt" : style["created_at"],
				"updatedAt" : style["updated_at"],
				"customerStyleCode" : style["customer_style_code"],
				"productBrief" : style["product_brief"],
				"archivedAt" : style["archived_at"],
				"completedAt" : style["completed_at"],
				"targetCosts" : style["target_costs"],
				"startDate" : style["start_date"],
				"targetDate" : style["target_date"],
				"orderType" : style["order_type"],
				"regionalMerchandiser" : style["regional_merchandiser"],
				"schemaVersion" : style["schema_version"],
				"board" : style["board_id"],
				"product" : style["product_id"],
		}
		style_data_list.append(data)
	return style_data_list
