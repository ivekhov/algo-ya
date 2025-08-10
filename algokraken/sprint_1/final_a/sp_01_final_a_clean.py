# https://contest.yandex.ru/contest/22450/run-report/134101202/

'''
Полное описание


Тимофей ищет место, чтобы построить себе дом. Улица, на которой он хочет жить, имеет длину n, 
то есть состоит из n одинаковых идущих подряд участков. 
Каждый участок либо пустой, либо на нём уже построен дом.

Общительный Тимофей не хочет жить далеко от других людей на этой улице. 
Поэтому ему важно для каждого участка знать расстояние до ближайшего пустого участка. 
Если участок пустой, эта величина будет равна нулю — расстояние до самого себя.

Помогите Тимофею посчитать искомые расстояния. Для этого у вас есть карта улицы. 
Дома в городе Тимофея нумеровались в том порядке, в котором строились, 
поэтому их номера на карте никак не упорядочены. 
Пустые участки обозначены нулями.

Формат ввода
В первой строке дана длина улицы —– n (1 ≤ n ≤ 106). 
В следующей строке записаны n целых неотрицательных чисел — номера домов и 
обозначения пустых участков на карте (нули). 
Гарантируется, что в последовательности есть хотя бы один ноль.
Номера домов (положительные числа) уникальны и не превосходят 109.

Формат вывода
Для каждого из участков выведите расстояние до ближайшего нуля. 
Числа выводите в одну строку, разделяя их пробелами.
--


Краткое описание

Есть массив длиной n
в массиве либо число, либо 0 
Нужно для каждого элемента массива посчитать расстояние до ближайшего 0
Если сам этот элемент None, то расстояние равно 0

Массив не упорядочен

Элементы в массиве принимают значение от 1 до 109

Формат вывода
Для каждого из элемента массива выведите расстояние до ближайшего нуля. 
Числа выводите в одну строку, разделяя их пробелами.

'''




from typing import List


def find_distance(cur_idx: int, left_zero_idx: int, right_zero_idx: int) -> int:
    '''Calculate minimal distance for current index between two zero indexes.'''
    if right_zero_idx - left_zero_idx == 0:
        return None
    
    dist_to_left = abs(cur_idx - left_zero_idx)
    dist_to_right = abs(cur_idx - right_zero_idx)

    return min(dist_to_left, dist_to_right)


def solve(houses: List[int]) -> str:
    '''Solution with one list as result.'''
    result = [None for _ in range(len(houses))]

    left_zero_idx, right_zero_idx = None, None

    for cur_idx, item in enumerate(houses):
        if item == 0:
            result[cur_idx] = 0
            right_zero_idx = cur_idx

            # left part
            if left_zero_idx is None:
                for item_idx in range(0, right_zero_idx):
                    result[item_idx] = abs(right_zero_idx - item_idx)
                
                left_zero_idx = right_zero_idx

            # center part
            elif left_zero_idx is not None:
                for item_idx in range(left_zero_idx, right_zero_idx):
                    dist = find_distance(item_idx, left_zero_idx, right_zero_idx)
                    result[item_idx] = dist
                left_zero_idx = right_zero_idx

    # right part
    if right_zero_idx < len(result):
        for item_idx in range(right_zero_idx, len(result)):
            result[item_idx] = abs(item_idx - right_zero_idx)

    return ' '.join(list(map(str, result)))


if __name__ == '__main__':
    with open('input.txt',  'r' ) as f:
        street = int(f.readline().rstrip())
        houses = f.readline().rstrip()
        houses = list(map(int, houses.split(' ')))
   
    with open('output.txt', 'w') as f:
        f.write(solve(houses))
