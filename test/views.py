from flask import request, jsonify
from flask.views import MethodView
from apps import *

class AppName(MethodView):
	"""docstring for ClassName"""

	def get(self, org, app):
		if org == 'sourceeasy':
			app = App(app)
			return jsonify({'data' : app.app()})
			return "app name"
		return "Organization is not valid"

