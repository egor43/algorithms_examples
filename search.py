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


def _get_smallest_node(table, visited_nodes):
    """
        Возвращает ближайший непосещенный элемент таблицы Дейкстры
        Params:
            table - таблица Дейкстры
            visited_nodes - посещенные элементы
        Return:
            ближайший непосещенный узел
    """
    smallest = None
    current_distance = None
    for node, info in table.items():
        if node in visited_nodes:
            continue
        distance = info["distance"]
        if (not current_distance) or (distance < current_distance):
            current_distance = distance
            smallest = info["node"]
    return smallest


def _get_root_distance(root_node, table):
    """
        Возвращает дистанцию до текущего элемента из таблицы Дейкстры
        Params:
            root_node - текущий узел от которого заполняется таблица
            table - таблица Дейкстры. 
                    Если отсутствует - создается новая.
        Return:
            расстояние до текущего элемента
    """
    root_distance = 0
    root_id = id(root_node)
    if root_id in table:
        root_distance = table[root_id]["distance"]
    return root_distance


def _calculate_table(root_node, table=None):
    """
        Заполнение таблицы Дейкстры
        Params:
            root_node - текущий узел от которого заполняется таблица
            table - таблица Дейкстры. 
                    Если отсутствует - создается новая.
        Return:
            таблица Дейкстры
    """
    if table is None:
        table = {}
    root_distance = _get_root_distance(root_node, table)
    # Обход соседей текущего элемента
    for neighbor in root_node["child"]:
        node = neighbor["node"]
        # Дистанция до соседа с учетом дистанции до текущего элемента
        distance = root_distance + neighbor["distance"]
        node_id = id(node)
        if node_id in table:
            table_distance = table[node_id]["distance"]
            if distance >= table_distance:
                continue
        table[node_id] = {"node": node, "distance": distance, "from": root_node}    
    return table


def dijkstra_search(root_node):
    """
        Поиск кротчайшего пути от root_node до других узлов
        Params:
            node - начальный узел
        Return:
            таблица кротчайших путей от root_node
    """
    visited_nodes = set()
    table = _calculate_table(root_node)
    next_node = _get_smallest_node(table, visited_nodes)
    while next_node:
        table = _calculate_table(next_node, table)
        visited_nodes.add(id(next_node))
        next_node = _get_smallest_node(table, visited_nodes)
    return table


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
    # Тестовый граф для алгоритма Дейкстры
    fin = {"name": "fin", "child": []}
    a_node = {"name": "A", "child": [{"distance": 1, "node": fin}]}
    b_node = {"name": "B", "child": [{"distance": 5, "node": fin}, {"distance": 3, "node": a_node}]}
    start = {"name": "start", "child": [{"distance": 6, "node": a_node}, {"distance": 2, "node": b_node}]}
    dijkstra_table = dijkstra_search(start)
    print(dijkstra_table)