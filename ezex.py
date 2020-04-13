import bottle
from bottle import run, route
import random


def generate_exercise():
    a, b = random.randrange(10), random.randrange(10)
    if a < b:
        a, b = b, a

    return ' '.join([str(a), "+", str(b), "="])


@route('/')
def home():
    res = ""
    for i in range(20):
        line = ""
        for j in range(4):

            line += generate_exercise() + '&emsp;&emsp;&emsp;&emsp;'
        res += '<h2>' + line
    return res

if __name__ == "__main__":
    run(host='0.0.0.0', port='9999')

app = bottle.default_app()
# print(home())
