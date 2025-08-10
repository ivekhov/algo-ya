# https://contest.yandex.ru/contest/22450/run-report/134101202/
import sys
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
