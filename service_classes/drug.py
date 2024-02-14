from datetime import datetime


class Drug:
    def __init__(self, sci_name: str, preparation: str, date: str, components: str):
        """
        Инициализатор класса препарата
        :param sci_name: имя ученого
        :param preparation: Название препарата
        :param date: Дата создания
        :param components: Компоненты препарата
        """
        self.sci_name = sci_name
        self.preparation = preparation
        self.date = datetime.strptime(date, '%Y-%m-%d')
        self.components = components.split()

    def print(self):
        print(self.sci_name, self.preparation, str(self.date).split()[0], self.components)

    def to_list(self):
        """
        Ф-я возвращает данные в виде списка
        :return: list
        """
        return [self.sci_name, self.preparation, str(self.date).split()[0], ' '.join(self.components)]
