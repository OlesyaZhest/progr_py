import json


# TODO решите задачу
def task() -> float:
    with open('input.json') as f:
        data = json.load(f)
    sum_of_products = 0
    for section in data:
        sum_of_products += section['score'] * section['weight']
    return f'{sum_of_products:.3f}'


print(task())
