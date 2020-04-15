import flask
import random


max_num = 20


def gen_one_ex():
    a, b = random.randrange(1, max_num), random.randrange(1, max_num)
    if a < b:
        a, b = b, a
    return ' '.join([str(a), random.choice(['+', '-']), str(b), "="])


def gen_ex_str(num):
    res = '<tr>'
    for i in range(num):
        res += '<td style="padding: 6px">' + gen_one_ex() + '</td>'
    res += '</tr>'
    return res


def gen_table(row, col):
    res = '<!DOCTYPE html><font style="font-size:24px"><b><table style="width:100%">'
    for i in range(row):
        res += gen_ex_str(col)
    res += '</table></b>'
    return res


app = flask.Flask(__name__)


@app.route('/')
def home():
    return gen_table(25, 4)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
