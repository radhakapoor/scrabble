from flask import Flask
#from flask_util_js import FlaskUtilJs


app = Flask(__name__)

#fujs = FlaskUtilJs(app)


from app import views