import service_classes as sc
from utils import read_file


def task3():
    """
    Решение задачи номер 3
    :return: None
    """
    while True:
        # очень круто открываем файл
        sci_data = read_file('scientist.txt', comma='#')
        dl = sc.DrugList(sci_data)
        dl.sort_on_date()  # сортируем по дате
        s = input("Введите дату в формате ДД.ММ.ГГГГ: \t")
        if s == 'эксперимент':
            break
        dl.get_all_on_date(s)
