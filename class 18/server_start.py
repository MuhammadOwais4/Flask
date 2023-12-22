from flask import Flask
from Controller.employee  import get_employees 
app = Flask(__name__)


app.add_url_rule('/employee', view_func=get_employees, methods=['GET'])


# Post method add employee

if __name__ == '__main__':
    app.run(
        port=5000,
        debug=True

    )

