import flask
import generate


app = flask.Flask(__name__)


@app.route('/')
def home():
    try:
        result = int(flask.request.args.get('max'))
    except:
        result = 10

    try:
        count = int(flask.request.args.get('num'))
    except:
        count = 80

    exs = generate.exercises(count, result)
    t = flask.Markup(generate.table(exs, 4))
    s = str(count) + " примеров до " + str(result)
    return flask.render_template('page.html', title=s, table=t)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9999)
