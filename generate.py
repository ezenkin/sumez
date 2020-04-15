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


def table(row, col):
    res = '<table style="width:100%">'
    for i in range(row):
        res += gen_ex_str(col)
    res += '</table></b>'
    return res
