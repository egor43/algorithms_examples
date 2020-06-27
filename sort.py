"""
    Примеры алгоритмов сортировки
"""


def _find_smallest(sequence):
    """
        Возвращает индекс минимального значения последовательности
        Params:
            sequence - последовательность
        Return:
            индекс минимального значения последовательности
    """
    smallest = sequence[0]
    smallest_index = 0
    for item_index, item in enumerate(sequence):
        if item < smallest:
            smallest = item
            smallest_index = item_index
    return smallest_index


def selection_sort(sequence):
    """
        Возвращает отсортированную последовательность.
        Используется алгоритм сортировки выбором.
        Params:
            sequence - последовательность
        Return:
            отсортированый список
    """
    sequence = sequence.copy()
    sorted_list = []
    for _ in range(len(sequence)):
        # Функцию _find_smallest можно заменить на: min(enumerate(sequence), key=lambda enum_tuple: enum_tuple[1])[0]
        smallest_index = _find_smallest(sequence)
        sorted_list.append(sequence.pop(smallest_index))
    return sorted_list


# Самотестирование
if __name__ == "__main__":
    unsorted_sequence = [5, 3, 8, 7, 6, 0, 1, 2, 9, 4]
    sorted_sequence = sorted(unsorted_sequence)
    # Проверяем, что сортировка выбором, действительно, сортирует
    assert selection_sort(unsorted_sequence) == sorted_sequence
