from test.models import *
from techpacksRepository import Techpacks
import json
from ChangeParamNameWithColumnName import techpackForeignTable
""" This 'techpack' variable contain the column name which we want to display """

techpackClass = Techpacks()

def getCreator(column_value, dict):
	return techpackClass.getUser({
		"table_name" : dict["table_name"],
		"column_name" : dict["column_name"],
		"column_value" : column_value
	})

def getCustomer(column_value, dict):
	return techpackClass.getCLS({
		"table_name" : dict["table_name"],
		"column_name" : dict["column_name"],
		"column_value" : column_value
	})

def function(techpack_list=[], page=0):
	techpack_data_list = []
	for techpackid in techpack_list:
		try:
			techpack = techpackClass.getTechpack(techpack_id = techpackid, page = page)[0]
		except :
			continue
		data = {
				"id" : techpack["id"],
				"version" : techpack["version"],
				"name" : techpack["name"],
				"styleCode" : techpack["style_code"],
				"category" : techpack["category"],
				"season" : techpack["season"],
				"stage" : techpack["stage"],
				"product" : techpack["product"],
				"productType" : techpack["product_type"],
				"sizeType" : techpack["size_type"],
				"sampleSize" : techpack["sample_size"],
				"visibility" : techpack["visibility"],
				"image" : techpack["image"],
				"revision" : techpack["revision"],
				"meta" : techpack["meta"],
				"parentId" : techpack["parent_id"],
				"creator" : getCreator(techpack["creator_id"], techpackForeignTable["creator_id"]) if techpack["creator_id"] else None,
				"customer" : getCustomer(techpack["customer_id"], techpackForeignTable["customer_id"]) if techpack['customer_id'] else None,
				"isLocked" : techpack["is_locked"],
				"isOwnerApproved" : techpack["is_owner_approved"],
				"isSeApproved" : techpack["is_se_approved"],
				"isSeOwned" : techpack["is_se_owned"],
				"isBuilderTechpack" : techpack["is_builder_techpack"],
				"isPublished" : techpack["is_published"],
				"lockedAt" : techpack["locked_at"],
				"lockedBy" : techpack["locked_by"],
				"unlockedAt" : techpack["unlocked_at"],
				"unlockedBy" : techpack["unlocked_by"],
				"archivedAt" : techpack["archived_at"],
				"completedAt" : techpack["completed_at"],
				"editLockedAt" : techpack["edit_locked_at"],
				"editLockedBy" : techpack["edit_locked_by"],
				"lastUpdatedBy" : techpack["last_updated_by"],
				"deletedAt" : techpack["deleted_at"],
				"createdAt" : techpack["created_at"],
				"updatedAt" : techpack["updated_at"],
				"specsRange" : techpack["specs_range"],
				"sizeRange" : techpack["size_range"],
				"workingSample" : techpack["working_sample_id"],
				"productionLockNote" : techpack["production_lock_note"],
				"editLockNote" : techpack["edit_lock_note"],
				"schemaVersion" : techpack["schema_version"],
		}
		techpack_data_list.append(data)
	return techpack_data_list
