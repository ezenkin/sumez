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


def exercises(count, max_num):
    res = []
    for i in range(count):
        res.append(gen_one_ex(max_num))
    return res


def generate_table_row(exs):
    res = '<tr>'
    for ex in exs:
        res += '<td style="padding: 6px">' + ex + '</td>'
    res += '</tr>'
    return res


def table(exs, cols):
    res = '<table style="width:100%">'
    row = []
    for ex in exs:
        row.append(ex)
        if len(row) >= cols:
            res += generate_table_row(row)
            row = []

    if len(row):
        res += generate_table_row(row)

    res += '</table></b>'
    return res
