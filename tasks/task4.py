import service_classes as sc
from utils import read_file


def task4():
    """
    Решение задачи номер 4
    :return: None
    """
    # очень круто открываем файл
    sci_data = read_file('scientist.txt', comma='#')
    dl = sc.DrugList(sci_data)
    dl.create_logins()  # делаем логины
