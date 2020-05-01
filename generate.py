import random


def sign(b):
    if b:
        return '+'
    return '-'


def gen_one_ex(max_res):
    a, b = 0, 0
    while a == b:
        a, b, s = random.randrange(1, max_res), random.randrange(1, max_res), True

    if a + b >= max_res:
        a, b, s = max(a, b), min(a, b), False

    return ' '.join([str(a), sign(s), str(b), "="])


def gen_ex_str(num):
    res = '<tr>'
    for i in range(num):
        res += '<td style="padding: 6px">' + gen_one_ex(20) + '</td>'
    res += '</tr>'
    return res


def table(row, col):
    res = '<table style="width:100%">'
    for i in range(row):
        res += gen_ex_str(col)
    res += '</table></b>'
    return res
