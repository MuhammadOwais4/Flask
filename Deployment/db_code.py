
from flask import Flask

import pymysql

app = Flask(__name__)

def mysqlconnect():
    # To connect MySQL database
    conn = pymysql.connect(
        host='owaismahasib.mysql.pythonanywhere-services.com',
        user='owaismahasib',
        password="Happybirthday12", # empty password
        db='owais',
        cursorclass=pymysql.cursors.DictCursor
    )
    print("db connected")
    return conn
    
def disconnect(conn):
  conn.close()

@app.route("/")
def home():
   return "home page"


@app.route("/connect-db")
def connect_db():
   
   db = mysqlconnect()
   disconnect(db)

   return "db connection"


# Driver Code
if __name__ == "__main__":
    app.run(
       debug=True,
       port=3000
    )
#45oEGWzm59zSMub
## create database
# find the button "Databases" and click
# you will see the form that requires you to enter mysql password, fill the form and hit the button "initialize Mysql". Store the password in safe place
# now you can find the following info in mysql settings i.e host, username and database
# database name would be something like "{YOUR_ACCOUNT_NAME}$default"
# NOTE: you can create more database if you like, every database you create will get prefixed by your account name following by a dollar sign



#------------------------------------------------------------------------------------------------------------------------------------------------
# from flask import Flask

# import pymysql

# app = Flask(__name__)

# def mysqlconnect():
#     # To connect MySQL database 
#     conn = pymysql.connect(
#         host='localhost',
#         user='root',
#         password="", # empty password
#         db='hr_db',
#         cursorclass=pymysql.cursors.DictCursor
#     )
  
#     print("db connected")
#     return conn


# @app.route("/connect-db")
# def connect_db():
   
#    db = mysqlconnect()
#    disconnect(db)

#    return "db connection"
# def mysqlconnect():
#     conn = pymysql.connect(
#         host =
#         user = 
#         password = 
#         db = 

#     )


