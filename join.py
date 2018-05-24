city = [
    {'id': 1, 'city': 'Москва', 'area': 'konkovo'},
    {'id': 2, 'city': 'Питер', 'area': 'kolpino'},
    {'id': 3, 'city': 'Казань', 'area': 'centr'}
]
person = [
    {'name': 'Андрей', 'cityid': 1, 'surname': 'kuzin'},
    {'name': 'Леонид', 'cityid': 2, 'surname': 'smirnov'},
    {'name': 'Сергей', 'cityid': 1, 'surname': 'fonarev'},
    {'name': 'Григорий', 'cityid': 4, 'surname': 'test'}
]


def pre(table, key1):
    pre_table = dict()
    table = list(table)
    for el in table:
        tmp_el = el.copy()
        del tmp_el[key1]
        if el[key1] not in pre_table:
            pre_table[el[key1]] = [tmp_el]
        else:
            pre_table[el[key1]].append(tmp_el)
    return pre_table


def join_inner(first_table, second_table, key1, key2):
    join_inner_table = []
    pre_table = pre(first_table, key1)
    for el in second_table:
        if el[key2] in pre_table:
            for el1 in pre_table[el[key2]]:
                result_dict = {}
                result_dict.update(el)
                result_dict.update(el1)
                result_dict.update({key1: el[key2]})
                join_inner_table.append(result_dict)
    return join_inner_table


def outer(inner_table, pre_table2, first_table, outer_keys2, key2):
    for key in outer_keys2:
        tmp_dict = dict()
        tmp_dict[key2] = key
        for el, el1 in pre_table2.items():
            if key == el:
                for el2 in el1:
                    tmp_dict.update(el2)
        for key in first_table[0]:
            tmp_dict[key] = None
        inner_table.append(tmp_dict)
    return inner_table


def join_outer(first_table, second_table, key1, key2):
    pre_1 = pre(first_table, key1)
    pre_2 = pre(second_table, key2)
    inner_table = join_inner(first_table, second_table, key1, key2)
    outer_keys1 = [key for key in pre_1.keys() if key not in pre_2.keys()]
    outer_keys2 = [key for key in pre_2.keys() if key not in pre_1.keys()]
    outer(inner_table, pre_1, second_table, outer_keys1, key1)
    return outer(inner_table, pre_2, first_table, outer_keys2, key2)


def join_right(first_table, second_table, key1, key2):
    pre_1 = pre(first_table, key1)
    pre_2 = pre(second_table, key2)
    inner_table = join_inner(first_table, second_table, key1, key2)
    outer_keys1 = [key for key in pre_1.keys() if key not in pre_2.keys()]
    return outer(inner_table, pre_1, second_table, outer_keys1, key1)


def join_left(first_table, second_table, key1, key2):
    pre_1 = pre(first_table, key1)
    pre_2 = pre(second_table, key2)
    inner_table = join_inner(first_table, second_table, key1, key2)
    outer_keys2 = [key for key in pre_2.keys() if key not in pre_1.keys()]
    return outer(inner_table, pre_table2, first_table, outer_keys2, key2)


for el in join_inner(city, person, 'id', 'cityid'):
    print(el)
