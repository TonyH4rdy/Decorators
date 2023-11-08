from decorator1 import logger

@logger('Generators')
def flat_generator(list_of_lists):
    '''Генератор, который принимает список списков
     и возвращает их плоское представление'''
    # Счётчик для текущего списка внутри списка списков:
    counter=-1
    while counter < len(list_of_lists)-1:
        counter += 1
        # Текущий список
        current_list = list_of_lists[counter]
        for el in current_list:
            yield el


list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]]

# Список выходных данных функции flat_generator :
results_list = []
# Распаковка  данных из генератора flat_generator:
for item in flat_generator(list_of_lists_1):
        results_list.append(item)

if __name__ == '__main__':
    print(f'Результат просчёта функции-генератора flat_generator :  {results_list=}')