import bottle
from bottle import run, route
import random


max_num = 20


def generate_exercise():
    a, b = random.randrange(max_num), random.randrange(max_num)
    if a < b:
        a, b = b, a
    res = ' '.join([str(a), random.choice(['+', '-']), str(b), "="])
    if len(res) < 9:
        res += '&ensp;' * (9 - len(res))
    return res


@route('/')
def home():
    res = ""
    for i in range(20):
        line = ""
        for j in range(4):

            line += generate_exercise() + '&emsp;&emsp;&emsp;'
        res += '<h2>' + line
    return res


if __name__ == "__main__":
    run(host='0.0.0.0', port='9999')

app = bottle.default_app()
# print(home())
