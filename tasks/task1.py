import service_classes as sc
from utils import read_file


def task1():
    """
    Решение задачи номер 1
    :return:
    """
    # очень круто открываем файл
    sci_data = read_file('scientist.txt', comma='#')
    dl = sc.DrugList(sci_data)
    dl.sort_on_date()  # сортируем по дате
    dl.find_apolorinol()  # находим подельников и так далее
    dl.get_original()  # делаем файл с оригинальными учеными
