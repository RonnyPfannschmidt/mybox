from flask import Flask


app = Flask(__name__
    static_file)




@app.route('/')
def index():
    return app.send_static_file('static/index.html')

