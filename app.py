from flask import Flask, render_template, url_for, make_response
app = Flask(__name__)

@app.route('/beta')
def beta():
    return render_template('index.html')

@app.route('/')
def new_html():
    return render_template('new.html')


@app.errorhandler(404)
def page_not_found(error):
    return make_response(render_template('404.htm'), 404)