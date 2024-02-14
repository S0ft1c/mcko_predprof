from random import shuffle


def perestanovka():
    """
    Ф-я возвращает список из случайно перемешанных чисел от 0 до 1023
    :return: list - список из чисел
    """
    arr = [i for i in range(0, 1024)]
    shuffle(arr)
    return arr
