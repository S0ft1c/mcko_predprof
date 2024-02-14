def read_file(filename: str, comma: str):
    """
    Ф-я быстро считывает все занчения из файла в виде списка списков (без первой строки и последней)
    Первую не считывает, потому как названия столбцов.
    Последнюю, так как она пустая.
    :param filename: Название файлы
    :param comma: Разделитель столбцов
    :return:
    """
    return list(map(lambda x: x.split(comma), open(filename, 'r', encoding='utf-8').readlines()[1:-1]))