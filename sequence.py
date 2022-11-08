from functools import lru_cache


@lru_cache(100)
def dec_seq(a):
    a1 = 0
    a2 = 0
    if a == 0:
        return 0
    if a == 1:
        return 1
    for d in str(dec_seq(a - 1)):
        a1 += int(d)
    for d in str(dec_seq(a - 2)):
        a2 += int(d)
    return a1 + a2


def digits_sequence(a):
    if a == 0:
        return 0
    if a == 1 or a == 2:
        return 1
    padded_a = a - 3
    index = padded_a % 24
    if Table.main_table.get(index):
        return Table.main_table.get(index)
    else:
        number = dec_seq(a)
        Table.main_table.update({index: number})
        return number


def initialize():
    print("initializing main_table")
    for i in range(3, 27):
        Table.main_table.update({i - 3: dec_seq(i)})
    print(f'main_table is : {Table.main_table}')


class Table:
    main_table = {}
