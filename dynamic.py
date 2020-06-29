"""
    Примеры алгоритмов динамического программирования
"""
from copy import deepcopy

# Задача о рюкзаке
guitar = {"name": "guitar", "cost": 1500, "weight": 1}
pleer = {"name": "pleer", "cost": 3000, "weight": 4}
notebook = {"name": "notebook", "cost": 2000, "weight": 3}
phone = {"name": "phone", "cost": 2000, "weight": 1}
items = [guitar, pleer, notebook, phone]

# Шаг веса
weight_step = 1
# Вместимость сумки
bag_size = 4

# Список весов
weights = [index + weight_step for index in range(bag_size)]
# Создание пустой таблицы
table = [[{"cost": 0, "items": []} for _ in range(bag_size)] for _ in range(len(items))]

# Заполняем первую строку таблицы
for weight_index in range(len(weights)):
    if items[0]["weight"] <= weights[weight_index]:
        table[0][weight_index]["cost"] = items[0]["cost"]
        table[0][weight_index]["items"] = [items[0]["name"]]

# Заполняем таблицу со второго элемента
for item_index in range(1, len(items)):
    for weight_index in range(len(weights)):
        # Предыдущая ячейка
        previous_rec = table[item_index - 1][weight_index]
        # Текущая ячейка
        current_rec = deepcopy(previous_rec)
        # Элемент, который обрабатываем
        item = items[item_index]

        # Если текущий элемент занимает все пространство и стоит больше, чем предыдущий элемент
        if (item["weight"] == weights[weight_index]) and (item["cost"] > previous_rec["cost"]):
            current_rec["cost"] = item["cost"]
            current_rec["items"] = [item["name"]]
        # Если текущий элемент занимает часть пространства
        elif item["weight"] < weights[weight_index]:
            # Получаем элемент, который убирается в оставшееся свободное пространство
            free_weight_rec = table[item_index - 1][weight_index - item["weight"]]
            max_current_cost = free_weight_rec["cost"] + item["cost"]
            # Если стоимость текущего элемента + стоимость элементов для свободного пространства выше чем у предыдущего
            if max_current_cost > previous_rec["cost"]:
                current_rec["cost"] = max_current_cost 
                current_rec["items"] = free_weight_rec["items"][:] 
                current_rec["items"].append(item["name"])
        table[item_index][weight_index] = current_rec

for row in table:
    print(row)
