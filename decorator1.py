import os
import  datetime


def logger(path):

    def __logger(old_function):

        def new_function(*args, **kwargs):
            # Список аргументы+результат
            item_list = []
            # print(f'Текущие дата и время - {datetime.datetime.now()}')
            date = datetime.date.today()
            print(f'Дата вызова функции - {date}')
            time = datetime.datetime.now().time()
            print(f'Время вызова функции -{time} ')
            name = old_function.__name__
            print(f'Имя функции- {name}')
            argums = f'{args=},{kwargs=}'
            print (argums)

            result = old_function(*args, **kwargs)
            print(f'Результат вызова функции - {result}')

            # Записываем в выходные данные значения кортежа args:
            for el in args:
                item_list.append(el)

            # Записываем в выходные данные значения словаря kwargs:
            for key,val in kwargs.items():
                item_list.append(val)

            item_list.append(result)
            item = tuple(item_list)
            print(f'Кортеж данных - {item}')

            # Запись в файл paths
            with open(path, 'a') as file:
                file.write(str(date))
                file.write('\n')
                file.write(str(time))
                file.write('\n')
                file.write(str(name))
                file.write('\n')
                file.write(argums)
                file.write('\n')
                file.write(str(result))
                file.write('\n')
                file.write(str(item))
                file.write("\n\n")
                print()
            return result

        return new_function

    return __logger

# Проверка работы кода
# Результаты работы кода записываются
# в файлы - test_1.log , test_2.log , test_3.log

paths_0 = ('test_1.log', 'test_2.log', 'test_3.log')

@logger('test_1.log')
def hello_world():
    return 'Hello World'

@logger('test_2.log')
def summator(a, b=0):
    return a + b

@logger('test_3.log')
def div(a, b):
    return a / b

# Проверка работы кода через исключения:

def test_2():
    paths = ('log_1.log', 'log_2.log', 'log_3.log')

    for path in paths:
        if os.path.exists(path):
            os.remove(path)

        @logger('log_1.log')
        def hello_world():
            return 'Hello World'

        @logger('log_2.log')
        def summator(a, b=0):
            return a + b

        @logger('log_3.log')
        def div(a, b):
            return a / b

        assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
        result = summator(2, 2)
        assert isinstance(result, int), 'Должно вернуться целое число'
        assert result == 4, '2 + 2 = 4'
        result = div(6, 2)
        assert result == 3, '6 / 2 = 3'
        summator(4.3, b=2.2)

    for path in paths:

        assert os.path.exists(path), f'файл {path} должен существовать'

        with open('log_2.log') as log_file:
            log_file_content = log_file.read()

        assert 'summator' in log_file_content, 'должно записаться имя функции'

        for item in (4.3, 2.2, 6.5):
            assert str(item) in log_file_content, f'{item} должен быть записан в файл'


if __name__ == '__main__':
    hello_world()
    summator(2, 2)
    div(6, 2)
    summator(4.3, b=2.2)
    test_2()