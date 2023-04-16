from typing import List


def car_paths(n: int, m: int) -> List[List[int]]:
    """
    Просчитать количество маршрутов до каждой клетки с учетом возможных перемещений.

    :param n: Количество строк в таблице
    :param m: Количество столбцов в таблице

    :return: Новую таблицу с посчитанным количеством маршрутов в каждую клетку
    """
        check = (n,m)
    if not isinstance(n, int) or not isinstance(m, int):
        raise TypeError

    if n < 0 or m < 0:
        raise  ValueError

    if n == 0 or m == 0:
        return 1


    table = []     #Cоздаем таблицу
    for _ in range(n):
        table.append([0] * m)

    for i in range(n):
        table[i][0] = 1

    for j in range(m):
        table[0][j] = 1

    for i in range(1, n):
        for j in range(1, m):
            table[i][j] = table[i - 1][j - 1] + table[i][j - 1] + table[i - 1][j]
    return table

if __name__ == '__main__':
    paths = car_paths(4, 2)
    print(paths[-1][-1])  # 7
