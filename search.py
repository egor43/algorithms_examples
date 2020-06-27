"""
    Примеры алгоритмов поиска
"""


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


# Самотестирование
if __name__ == "__main__":
    # Простое тестирование binary_search
    searched_index = binary_search(2, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    assert searched_index == 1
