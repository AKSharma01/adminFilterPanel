taskTable = {
	"id" : "id",
	"title" : "title",
	"description" : "description",
	"creator" : "creator_id",
	# "is_assignee_group" : "is_assignee_group",
	"dueDate" : "due_date",
	"seen" : "seen",
	"isSubmitted" : "is_submitted",
	"isCompleted" : "is_completed",
	"submissionDate" : "submission_date",
	"completionDate" : "completion_date",
	"priority" : "priority_id",
	"location" : "location",
	"status" : "status_id",
	"deletedAt" : "deleted_at",
	"createdAt" : "created_at",
	"updatedAt" : "updated_at",
	"tna_itemId" : "tna_item_id",
	"archivedAt" : "archived_at",
	"createdFrom" : "created_from",
	# "created_from_id" : "created_from_id",
	# "google_calendar_id" : "google_calendar_id",
	"checklist" : "checklist",
	"line" : "line_id",
	"style" : "style_id",
	"customer" : "customer_id",
	"needApproval" : "need_approval",
	"isApproved" : "is_approved",
	"starter" : "starter_id",
	"submitter" : "submitter_id",
	"schemaVersion" : "schema_version"

}

taskForeignTable = {
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
	# "google_calendar_id"
	"line_id" : {
		"table_name" : "lines",
		"column_name" : "id",
		"column_to_find" : "code"
	},
	"status_id" : {
		"table_name" : "task_status",
		"column_name" : "id",
		"column_to_find" : "status"
	},
	"style_id" : {
		"table_name" : "styles",
		"column_name" : "id",
		"column_to_find" : "code"
	}
	# "tna_item_id"
}


