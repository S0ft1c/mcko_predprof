from random import choice

alph = list('qwertyuiopasdfghjklzxcvbnm' + 'qwertyuiopasdfghjklzxcvbnm'.upper() + '1234567890')


def passwd_generator():
    """
    Ф-я генерирует пароль из строчных, заглавных и цифр
    :return: str - пароль
    """
    passwd = ''
    for _ in range(10):
        passwd += choice(alph)
    return passwd
