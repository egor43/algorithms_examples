"""
    Примеры алгоритмов поиска
"""
from collections import deque


def binary_search(item, sorted_list):
    """
        Бинарный поиск
        Params:
            item - искомый элемент
            sorted_list - отсортированый список
        Result:
            позиция искомого элемента или None
    """
    low = 0
    high = len(sorted_list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = sorted_list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


def graph_search(algorithm, root_node, check_func):
    """
        Поиск по графу в ширину.
        Params:
            algorithm - алгоритм поиска по графу.
                        Допустимые значения: "BFS" и "DFS"
            root_node - узел графа от которого будет осуществлен поиск.
                        Используются ноды вида: {"name": "node_name", "child": [node_1, node_2, ...]}
            check_func - функция проверяет является ли текущий элемент - искомым
        Return:
            элемент, удовлетворяющий проверке check_func
    """
    # Посещенные узлы
    visited_nodes = set()
    # Очередь узлов, ожидающих проверки
    nodes = deque([root_node])
    # Метод получения следующего узла зависит от алгоритма
    if algorithm == "BFS":
        get_next_node = nodes.popleft
    elif algorithm == "DFS":
        get_next_node = nodes.pop
    while nodes:
        current_node = get_next_node()
        if not id(current_node) in visited_nodes:
            if check_func(current_node):
                return current_node
            nodes.extend(current_node["child"])
            visited_nodes.add(id(current_node))
    return None


# Самотестирование
if __name__ == "__main__":
    # Простое тестирование binary_search
    searched_index = binary_search(2, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    assert searched_index == 1

    # Строим тестовый граф
    anuged = {"name": "Anuged", "child": []}
    paggie = {"name": "Paggie", "child": []}
    johny = {"name": "Johny",  "child": []}
    tom = {"name": "Tom", "child": []}
    bob = {"name": "Bob", "child": [anuged, paggie]}
    clare = {"name": "Clare", "child": [tom, johny]}
    alice = {"name": "Alice", "child": [paggie]}
    you = {"name": "You", "child": [bob, alice, clare]}
    assert paggie == graph_search("BFS", you, lambda node: node["name"] == "Paggie")
    assert anuged == graph_search("DFS", you, lambda node: node["name"] == "Anuged")
