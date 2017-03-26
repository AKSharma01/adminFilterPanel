techpackTable = {
	"id" : "id",
	"version" : "version",
	"name" : "name",
	"styleCode" : "style_code",
	"category" : "category",
	"season" : "season",
	"stage" : "stage",
	"product" : "product",
	"productType" : "product_type",
	"sizeType" : "size_type",
	"sampleSize" : "sample_size",
	"visibility" : "visibility",
	"image" : "image",
	"revision" : "revision",
	"meta" : "meta",
	# "parent_id" : "parent_id",
	"creator" : "creator_id",
	"customer" : "customer_id",
	"isLocked" : "is_locked",
	# "is_owner_approved" : "is_owner_approved",
	# "is_se_approved" : "is_se_approved",
	# "is_se_owned" : "is_se_owned",
	# "is_builder_techpack" : "is_builder_techpack",
	"isPublished" : "is_published",
	"lockedAt" : "locked_at",
	"lockedBy" : "locked_by",
	"unlockedAt" : "unlocked_at",
	"unlockedBy" : "unlocked_by",
	"archived" : "archived_at",
	"completedAt" : "completed_at",
	# "edit_locked_at" : "edit_locked_at",
	"editLockedBy" : "edit_locked_by",
	"lastUpdatedBy" : "last_updated_by",
	"deletedAt" : "deleted_at",
	"createdAt" : "created_at",
	"updatedAt" : "updated_at",
	"specsRange" : "specs_range",
	"sizeRange" : "size_range",
	"workingSample" : "working_sample_id",
	"productionLockNote" : "production_lock_note",
	"editLockNote" : "edit_lock_note",
	"schemaVersion" : "schema_version",
}

techpackForeignTable = {
	"creator_id" : {
		"table_name" : "users",
		"column_name" : "id",
		"column_to_find" : "email"
	},
	"customer_id" : {
		"table_name" : "customers",
		"column_name" : "id",
		"column_to_find" : "code"
	},
	"working_sample_id" : {
		"table_name" : "techpacks2_samples",
		"column_name" : "id",
		"column_to_find" : "techpack_id"
	}	
}

techpackFilterByKey = ["customer", "creator", "archived", "styleCode", "stage", "category", "season", "version"]

