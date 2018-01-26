import os
from flask import Flask,render_template,url_for, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

PORT = int( os.environ.get("PORT"))

app.run(host='0.0.0.0', port=PORT)
print("app is running on port ", PORT)
