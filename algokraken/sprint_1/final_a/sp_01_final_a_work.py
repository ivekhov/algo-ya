'''
Тимофей ищет место, чтобы построить себе дом. Улица, на которой он хочет жить, 
имеет длину n, то есть состоит из n одинаковых идущих подряд участков. Каждый участок либо пустой, либо на нём уже построен дом.

Общительный Тимофей не хочет жить далеко от других людей на этой улице. Поэтому ему 
важно для каждого участка знать расстояние до ближайшего пустого участка. Если участок пустой, эта величина будет равна нулю — расстояние до самого себя.

Помогите Тимофею посчитать искомые расстояния. Для этого у вас есть карта улицы. 
Дома в городе Тимофея нумеровались в том порядке, в котором строились, поэтому их номера на карте никак не упорядочены. Пустые участки обозначены нулями.

Формат ввода
В первой строке дана длина улицы —– n (1 ≤ n ≤ 106). В следующей строке записаны n целых неотрицательных чисел — 
номера домов и обозначения пустых участков на карте (нули). Гарантируется, что в последовательности есть хотя бы один ноль. 
Номера домов (положительные числа) уникальны и не превосходят 109.

## 1

6
0 7 9 4 8 20

0 1 2 3 4 5

## 2

5
0 1 4 9 0

[0, 1, 2, 1, 0]


12
0 1 4 9 0 3 7 11 20 0 2 7 

indexes:
[0, 1, 2, 3, 4, 5, 6, 7, 8]

zero indexes:
[0, 4, 9]

cur_idx: 
1


resp: 
0 1 2 1 0


14
0 3 41 0 0 0 0 0 49 0 0 56 0 88

correct
0 1 1 0 0 0 0 0 1 0 0 1 0 1

0 1 1 0 0 0 0 0 1 0 0 1 0 1
0 1 1 0 0 0 0 0 1 0 0 1 0 1
0 1 1 0 0 0 0 0 1 0 0 1 0 1



15
9 0 3 41 0 0 0 0 0 49 0 0 56 0 88

1 0 1 1 0 0 0 0 0 1 0 0 1 0 1

1 0 1 1 0 0 0 0 0 1 0 0 1 0 1
1 0 1 1 0 0 0 0 0 1 0 0 1 0 1
0 0 0 1 1 0 0 0 0 0 1 0 0 1 0 1
  0 0 0 1 1 0 0 0 0 0 1 0 0 1 0 1
  0 1 0 1 1 0 0 0 0 0 1 0 0 1 0 1
  0 1 1 0 0 0 0 0 1 0 0 1 0 1
  0 1 1 0 0 0 0 0 1 0 0 1 0 1



12
99 0 100 72 43 49 0 51 19 61 93 31

1 0 1 2 2 1 0 1 2 3 4 5
1 0 1 2 2 1 0 1 2 3 4 5 6
1 0 1 2 2 1 0 1 2 3 2 1

'''

import sys
import time
from typing import List


def find_distance(cur_idx: int, left_zero_idx: int, right_zero_idx: int) -> int:
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


def __solve(houses: List[int]) -> str:
    result = []
    zero_indexes = []
    for idx, item in enumerate(houses):
        if item == 0:
            zero_indexes.append(idx)
            
    if len(zero_indexes) == 1:
        for cur_idx in range(len(houses)):
            result.append(abs(zero_indexes[0] - cur_idx))
    else:
        # left part
        if zero_indexes[0] != 0:
            for cur_idx in range(0, zero_indexes[0]):
                result.append(abs(zero_indexes[0] - cur_idx))
        
        # center parts        
        for idx in range(1, len(zero_indexes)):
            left_zero_idx = zero_indexes[idx-1]
            right_zero_idx = zero_indexes[idx]

            for cur_idx in range(left_zero_idx, right_zero_idx):
                dist = find_distance(cur_idx, left_zero_idx, right_zero_idx)
                result.append(dist)

        # right part 
        if zero_indexes[-1] < len(houses):
            for cur_idx in range(zero_indexes[-1], len(houses)):
                result.append(abs(zero_indexes[-1] - cur_idx))
    
    return ' '.join(list(map(str, result)))



###

def solve_work_but_complex(houses: List[int]) -> str:
    result = []
    zero_indexes = []
    for idx, item in enumerate(houses):
        if item == 0:
            zero_indexes.append(idx)    
    if len(zero_indexes) == 1:
        for cur_idx in range(len(houses)):
            result.append(abs(zero_indexes[0] - cur_idx))
    else:

        # left part
        if zero_indexes[0] != 0:
            for cur_idx in range(0, zero_indexes[0]):
                result.append(abs(zero_indexes[0] - cur_idx))
        
        # center parts        
        for idx in range(1, len(zero_indexes)):
            left_zero_idx = zero_indexes[idx-1]
            right_zero_idx = zero_indexes[idx]

            for cur_idx in range(left_zero_idx, right_zero_idx):
                dist = find_distance(cur_idx, left_zero_idx, right_zero_idx)
                result.append(dist)

        # right part 
        if zero_indexes[-1] < len(houses):
            for cur_idx in range(zero_indexes[-1], len(houses)):
                result.append(abs(zero_indexes[-1] - cur_idx))
    
    return ' '.join(list(map(str, result)))

def solve_wrong(houses, street):
    '''solve_pairs_zero.'''
    result = []
    zero_indexes = []

    for idx, item in enumerate(houses):
        if item == 0:
            zero_indexes.append(idx)

        # print(f'zero_indexes: {zero_indexes}')
    for cur_idx, item in enumerate(houses):
        slider = 0
        if item != 0:
            
            if len(zero_indexes) == 1:
                left_zero_idx = zero_indexes[0]
                right_zero_idx = zero_indexes[0]

                dist = find_distance(cur_idx, left_zero_idx, right_zero_idx)
                result.append(dist)
            
            else:
                left_zero_idx = zero_indexes[slider]
                right_zero_idx = zero_indexes[slider+1]

                if cur_idx < right_zero_idx:
                    dist = find_distance(cur_idx, left_zero_idx, right_zero_idx)
                    result.append(dist)
                else:
                    if (slider+1) < len(zero_indexes):
                        slider += 1
                        left_zero_idx = zero_indexes[slider]
                        right_zero_idx = zero_indexes[slider+1]
                        dist = find_distance(cur_idx, left_zero_idx, right_zero_idx)
                        result.append(dist) 

                    else:
                        left_zero_idx = zero_indexes[slider]
                        right_zero_idx = zero_indexes[slider]
                        dist = find_distance(cur_idx, left_zero_idx, right_zero_idx)
                        result.append(dist)
                

        elif item == 0:
            result.append(0)

    return ' '.join(list(map(str, result)))



def __find_distance_to_closest_zero_idx(cur_idx, zero_indexes, street):
    '''Slow x10 on 10 ** 9 length than needed. Works correctly.'''
    min_dist = street

    for zero_idx in zero_indexes:
        dist = abs(cur_idx - zero_idx)
        if dist < min_dist:
            min_dist = dist    
    return min_dist


def __solve_naive(houses, street):
    result = []
    # find indexes of all zeros ex: [0, 4] # fast
    zero_indexes = []
    for idx, item in enumerate(houses):
        if item == 0:
            zero_indexes.append(idx)

    # testing
    # return zero_indexes # fast
    # return ' '.join(list(map(str, zero_indexes))) # fast
    
    
    # iterate for each item if not zero index  and 
    # find closest index zero
    
    for idx, item in enumerate(houses):
        if item != 0:
            
            # ToDo: speed up 
            result.append(find_distance_to_closest_zero_idx(idx, zero_indexes, street))
            
        elif item == 0:
            result.append(0)

    return ' '.join(list(map(str, result)))


if __name__ == '__main__':
    # from console: 
    
    # start = time.time()
    # street = int(sys.stdin.readline().rstrip())
    # houses = sys.stdin.readline().rstrip()
    # houses = list(map(int, houses.split(' ')))
    # print(solve(houses))

    # end = time.time()
    # print(f'{(end - start) } seconds')
    
    ## ----------
    
    # from file: 

    start = time.time()

    with open('input.txt',  'r' ) as f:
        street = int(f.readline().rstrip())
        houses = f.readline().rstrip()
        houses = list(map(int, houses.split(' ')))
   
    with open('output.txt', 'w') as f:
        f.write(solve(houses))
        
    end = time.time()
    print(f'{(end - start) } seconds')

