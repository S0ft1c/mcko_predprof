import tasks


def main():
    task_num = input('Введите число задания, которое вы хотите протестировать: ').strip()
    if task_num == '1':
        tasks.task1()
    if task_num == '2':
        tasks.task2()
    if task_num == '3':
        tasks.task3()
    if task_num == '4':
        tasks.task4()
    if task_num == '5':
        tasks.task5()


if __name__ == '__main__':
    main()
