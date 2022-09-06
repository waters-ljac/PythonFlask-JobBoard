# import flask

# app = flask.Flask(__name__)

# @app.route('/')
# @app.route('/jobs')
# def jobs():
#     return flask.render_template('index.html')

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/jobs')
def jobs():
    return render_template('index.html')
