"""
This module implements some functions based on linear search algo
"""
from typing import List


def min_search(arr: List[int]) -> int:
    """
    Функция для поиска минимума в массиве

    :param arr: Массив целых чисел
    :return: Индекс первого вхождения элемента в массиве
    """
            if len(arr) == 0:
        raise ValueError("Список не может быть пустым")
    min_index = 0
    min_meaning = arr[0]
    for i in range(len(arr)):
        if arr[i] < min_meaning:
            min_meaning = arr[i]
            min_index = i
    return min_index
