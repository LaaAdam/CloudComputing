from flask import flask

app = Flask(_name_)

@app.route('/')
def hello_world():
    return 'Hello ! '

if_name_ == "_main_":
    app.run(host='0.0.0.0, port=5000')