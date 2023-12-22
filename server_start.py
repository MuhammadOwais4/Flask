from flask import Flask, request


app= Flask(__name__)

# Get method 
@app.route("/")
def home():
    return "home page"
# second api
@app.route("/profile")
def profile():
    return "profile page"
# third api with post 
# Get Reqest
@app.route("/input/get/query_string",methods=
['Get'])
def inputgetquery_string():
    print(request.args)
    print("query string 1",request.args.get("key1"))
    print("query string 1",request.args.get("key2"))
    return "Get Qurey string"
# four api path parameter
@app.route("/input/get/path_parameter")
def inputgetpath_parameter():
    return "path parameter"

# five api user path parameter
@app.route("/input/get/path_parameters/<id>")
def inputgetpath_parameters(id):
    return f"path parameter {id}"




app.run(
 port=3000,
 debug=True
)
