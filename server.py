from flask import Flask, render_template, url_for
app = Flask(__name__)

#style ways
url_for('css', filename='main.css')

#image ways
url_for('img', filename='bg.jpg')

@app.route('/')
def hello_world():
    return render_template('index.html')