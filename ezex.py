import flask
import generate


app = flask.Flask(__name__)


@app.route('/')
def home():
    try:
        max_num = int(flask.request.args.get('max_num'))
    except:
        max_num = 10

    try:
        count = int(flask.request.args.get('count'))
    except:
        count = 100

    exs = generate.exercises(count, max_num)
    t = flask.Markup(generate.table(exs, 4))
    s = str(count) + " примеров до " + str(max_num)
    return flask.render_template('page.html', title=s, table=t)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9999)
