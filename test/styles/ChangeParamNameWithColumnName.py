styleTable = {
	"id" : "id",
	"code" : "code",
	"name" : "name",
	"line" : "line_id",
	# "tna" : "tna_id",
	"techpack" : "techpack_id",
	"order" : "order_id",
	"flat" : "flat",
	"deletedAt" : "deleted_at",
	"createdAt" : "created_at",
	"updatedAt" : "updated_at",
	"customerStyleCode" : "customer_style_code",
	"productBrief" : "product_brief",
	"archived" : "archived_at",
	"completedAt" : "completed_at",
	"targetCosts" : "target_costs",
	"startDate" : "start_date",
	"targetDate" : "target_date",
	"orderType" : "order_type",
	"regionalMerchandiser" : "regional_merchandiser",
	"schemaVersion" : "schema_version",
	"board" : "board_id",
	"product" : "product_id",
}

styleForeignTable = {
	"line_id" : {
		"table_name" : "lines",
		"column_name" : "id",
		"column_to_find" : "code"
	},
	"order_id" : {
		"table_name" : "orders",
		"column_name" : "id",
		"column_to_find" : "code"
	},
	"regional_merchandiser" : {
		"table_name" : "users",
		"column_name" : "id",
		"column_to_find" : "email"
	},
	"techpack_id" : {
		"table_name" : "techpacks2",
		"column_name" : "id",
		"column_to_find" : "style_code"
	}
}

styleFilterByKey = ["code", "regionalMerchandiser", "customerStyleCode", "orderType", "category", "season", "version"]

