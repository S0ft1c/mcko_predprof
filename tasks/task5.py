import service_classes as sc
from utils import read_file


def task5():
    """
    Решение задачи номер 5
    :return: None
    """
    # очень круто открываем файл
    sci_data = read_file('scientist.txt', comma='#')
    dl = sc.DrugList(sci_data)
    dl.create_hash()  # делаем хэши
