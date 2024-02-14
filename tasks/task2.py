import service_classes as sc
from utils import read_file


def task2():
    """
    Решение задачи номер 2
    :return: None
    """
    # очень круто открываем файл
    sci_data = read_file('scientist.txt', comma='#')
    dl = sc.DrugList(sci_data)
    dl.sort_on_date()  # сортируем по дате
    dl.head()  # крутой вывод МОЕЙ ф-ей
