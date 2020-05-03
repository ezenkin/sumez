import flask
import generate


app = flask.Flask(__name__)


@app.route('/')
def home():
    max_num = flask.request.args.get('max_num')
    count = flask.request.args.get('count')
    # TODO: check parameters
    exs = generate.exercises(int(count), int(max_num))
    print(exs)
    t = flask.Markup(generate.table(exs, 4))
    return flask.render_template('page.html', table=t)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9999)
