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
        # Функцию _find_smallest можно заменить на: min(enumerate(sequence), key=lambda enum_tuple: enum_tuple[1])[0]        #smallest_index = 
        smallest_index = _find_smallest(sequence)
        sorted_list.append(sequence.pop(smallest_index))
    return sorted_list


def quick_sort(sequence):
    """
        Возвращает отсортированную последовательность.
        Используется рекурсивный алгоритм быстрой сортировки
        Params:
            sequence - последовательность
        Return:
            отсортированый список
    """
    # Базовый случай
    if len(sequence) < 2:
        return sequence
    else:
        # Индекс опорного элемента (выбираем средний)
        pivot_index = len(sequence) // 2
        # Опроный элемент
        pivot = sequence[pivot_index]
        # Подмассив всех элементов меньших опорного
        less = []
        # Подмассив всех элементов больших опорного
        greater = []
        for element in sequence[:pivot_index] + sequence[pivot_index+1:]:
            if element > pivot:
                greater.append(element)
            else:
                less.append(element)
        return quick_sort(less) + [pivot] + quick_sort(greater)


# Самотестирование
if __name__ == "__main__":
    unsorted_sequence = [5, 3, 8, 7, 6, 0, 1, 2, 9, 4]
    sorted_sequence = sorted(unsorted_sequence)
    # Тестирование сортировки выбором
    assert selection_sort(unsorted_sequence) == sorted_sequence
    # Тестирование быстрой сортировки
    assert quick_sort(unsorted_sequence) == sorted_sequence
