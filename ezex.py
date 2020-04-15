import flask
import generate


app = flask.Flask(__name__)


@app.route('/')
def home():
    t = flask.Markup(generate.table(25, 4))
    return flask.render_template('page.html', table=t)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9999)
