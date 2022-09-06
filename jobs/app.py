import flask

@route('/')
@route('/jobs')
def jobs():
    return flask.render_template('index.html')

app = flask.Flask(__name__)
