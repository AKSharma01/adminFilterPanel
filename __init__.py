from flask import Flask
from flask_cors import CORS
from test.urls import urls
from models.models import *

app = Flask(__name__)
CORS(app)

for url in urls:
    app.add_url_rule(url[0], methods = url[1], view_func = url[2])

if __name__ =='__main__':
    app.run(debug = True)
    
