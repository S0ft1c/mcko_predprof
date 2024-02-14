from .drug import Drug
from datetime import datetime
from utils import passwd_generator, perestanovka


class DrugList:
    def __init__(self, arr: list):
        """
        Инициализатор класса списка препаратов
        :param arr: Список, состоящий из списков, которые содержат информацию о препарате
        """
        self.__arr = []
        for el in arr:
            self.__arr.append(
                Drug(el[0], el[1], el[2], el[3])
            )

    def print(self):
        for el in self.__arr:
            el.print()

    def sort_on_date(self):
        self.__arr.sort(key=lambda x: x.date)

    def find_apolorinol(self):
        """
        Функция делаем отправку в полицию по поводу Аллопуринола
        :return: None
        """
        pr = [el for el in self.__arr if el.preparation == 'Аллопуринол']
        print('Разработчиками Аллопуринола были такие люди (результаты выведите в порядке возрастания даты): ')
        for el in pr[1:]:
            print(f'{el.sci_name} - {str(el.date).split()[0]}')
        print(f'Оригинальный рецепт принадлежит: {pr[0].sci_name}')

    def write_to_file(self, filename: str, data=None):
        """
        Ф-я записывает необходимые данные в нужный файл
        :param filename:
        :param data:
        :return:
        """
        if data is None:
            data = self.__arr

        # открываем файл
        sci_origin_file = open('scientist_origin.txt', 'w+', encoding='utf-8')
        sci_origin_file.write('ScientistName#preparation#date#components\n')

        # записываем данные
        for el in data:
            sci_origin_file.write(
                f'{el.sci_name}#{el.preparation}#{str(el.date).split()[0]}#{" ".join(el.components)}\n')
        sci_origin_file.close()

    def get_original(self):
        """
        Ф-я делаем новые файл с названием scientist_origin.txt и оригинальными препаратами там
        :return: None
        """
        drugs = set()
        data = []
        for el in self.__arr:
            if el.preparation not in drugs:
                data.append(el)
            drugs.add(el.preparation)
        self.write_to_file('scientist_origin.txt', data)  # записываем в файл

    def get_all_on_date(self, date: str):
        """
        Ф-я выдает всех ученых по нужной дате
        :param date: Дата в формате ДД.ММ.ГГГГ
        :return:
        """
        date = list(map(lambda x: int(x) if x[0] != '0' else int(x[1:]), date.split('.')))
        self.sort_on_date()  # на всякий
        date = datetime(day=date[0], month=date[1], year=date[-1])

        l, r = 0, len(self.__arr)
        m = -1
        while l != r + 1 and l + 1 != r:
            m = (r + l) // 2
            if self.__arr[m].date > date:
                r = m
            else:
                l = m

        cnt = 0
        for el in self.__arr[m:]:
            if el.date == date:  # если это нужная дата
                print(f'Ученый {el.sci_name} создал препарат: {el.preparation} - {el.date}')
                cnt += 1
            else:  # если нет, значит все
                break

        if not cnt:  # если никого не бюло найдено
            print('В этот день ученые отдыхали')

    def create_logins(self):
        """
        Ф-я добвляет логины и пароли и записывает это все в scientist_password.csv
        :return:
        """
        data = []
        for el in self.__arr:
            pr = el.to_list()
            login = pr[0].split()[0] + '_' + pr[0].split()[1][0] + pr[0].split()[-1][0]
            passwd = passwd_generator()
            pr.extend(
                [login, passwd]
            )
            data.append(pr)

        with open('scientist_password.csv', 'w+', encoding='utf-8') as file:
            file.write('ScientistName#preparation#date#components#login#password\n')

            for el in data:
                file.write(
                    '#'.join(el) + '\n'
                )

    def create_hash(self):
        """
        Ф-я добавляет хэш и записывает в scientist scientist_with_hash.csv
        :return: None
        """
        data = []
        pere = perestanovka()
        for el in self.__arr:
            pr = el.to_list()
            ha = []  # временный массив для хэша
            for i in pr[0]:
                ha.append(pere[ord(i) % 1024])

            pr = [str(sum(ha) % 2048)] + pr  # аккуратно добавляем вперед
            data.append(pr)

        with open('scientist_with_hash.csv', 'w+', encoding='utf-8') as file:
            file.write('hash#ScientistName#preparation#date#components\n')

            for el in data:
                file.write(
                    '#'.join(el) + '\n'
                )

    def head(self, n: int = 5):
        """
        Ф-я выводит первые n элементов. Изначально это 5
        :param n: Количество первых элементов
        :return: None
        """
        for el in self.__arr[:n]:
            el.print()
