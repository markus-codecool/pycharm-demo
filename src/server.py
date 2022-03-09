import flask

app = flask.Flask(__name__)


@app.route('/')
def main_endpoint():
    return flask.render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
