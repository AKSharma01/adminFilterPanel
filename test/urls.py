from views import *

urls = [
	('/<org>/<app>', ['GET'], AppName.as_view('app'))

]