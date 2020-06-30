"""
    Примеры алгоритмов K-ближайших соседей
"""
import math


def minimax_normalization(attribute_list):
    """
        Функция минимаксной нормализации атрибутов
        Params:
            attribute_list - список атрибутов
        Result:
            список нормализованных атрибутов
    """
    min_attr = min(attribute_list)
    max_attr = max(attribute_list)
    return [(attr - min_attr) / (max_attr - min_attr) for attr in attribute_list]


def calculate_distance(first_attrubutes, second_attributes):
    """
        Функция вычисления расстояния между двумя наборами числовых атрибутов
        Params:
            first_attrubutes - первый набор числовых атрибутов
            second_attributes - второй набор числовых атрибутов
        Return:
            расстояние между наборами числовых атрибутов
    """
    root_expression = 0
    for attribute_index in range(len(first_attrubutes)):
        root_expression += (first_attrubutes[attribute_index] - second_attributes[attribute_index])**2
    return math.sqrt(root_expression)


def k_nearest_neighbors(neighbors, explore_object, k):
    """
        Вычисление K ближайших соседей
        Params:
            neighbors - известные объекты с наборами числовых атрибутов
                        [{"attributes": [number, number,...], another_fields...},
                         {"attributes": [number, number,...], another_fields...},
                         ....]
            explore_object - объект с набором числовых атрибутов для которого необходимо найти соседей
                             {"attributes": [number, number,...], another_fields...}
            k - количество ближайших соседей
        Return:
            ближайшие объекты
    """
    # Полчаем и нормализуем атрибуты изучаемого объекта
    explore_attributes = minimax_normalization(explore_object["attributes"])
    distances = []
    # Вычисляем расстояния до всех известных объектов
    for neighbor in neighbors:
        neighbor_attributes = minimax_normalization(neighbor["attributes"])
        distance = calculate_distance(explore_attributes, neighbor_attributes)
        distances.append((distance, neighbor))
    # Получаем K ближайших соседей
    distances.sort(key=lambda item: item[0])
    return [ item[1] for item in distances[:k]]


# Данные об оценках пользователей для 5 товаров (оценка от 1 до 10)
alice = {"attributes": [1, 5, 2, 9, 3], "name": "Alice"}
bob = {"attributes": [3, 7, 8, 10, 2], "name": "Bob"}
tom = {"attributes": [1, 4, 1, 7, 3], "name": "Tom"}
neighbors = [alice, bob, tom]

nearest_neighbors = k_nearest_neighbors(neighbors, {"attributes": [1, 2, 3, 4, 5]}, 2)
print("Ближайшие соседи:")
for neighbor in nearest_neighbors:
    print(neighbor["name"])
