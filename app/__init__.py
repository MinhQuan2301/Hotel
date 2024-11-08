from urllib.parse import quote
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask import Flask
from flask_login import LoginManager


app = Flask(__name__)
app.secret_key = "1234567890!@#$%^&*()qwertyuioplkjhgfdsazxcvbnm,./ASDFGHJKLZMXNCBVQWERTYUIOP"
app.config["SQLALCHEMY_DATABASE_URI"] = ("mysql+pymysql://root:%s@localhost/dbhotel?charset=utf8mb4"
                                         % quote("d@Ikaquan2301"))
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True



db = SQLAlchemy(app)

admin = Admin(app=app, name='Kho Dữ Liệu', template_mode='bootstrap4')

login = LoginManager(app=app)
