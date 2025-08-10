# https://contest.yandex.ru/contest/22450/run-report/134098937/

# from collections import Counter
from typing import List


def preprocess(row: str) -> List[int]:
    '''Preprocess raw string into list of integers.'''
    chars = [int(char) if char.isnumeric() else None for char in row ]
    return chars


def __solve(k: int, data: List[int]) -> int:
    '''Solution with Counter and dict.'''
    counter = dict(Counter(data))
    score = 0

    for cycle in range(1, 10):
        if cycle in counter.keys():
            if k * 2 >= counter.get(cycle):
                score += 1
    
    return score


def solve(k: int, data: List[int]) -> int:
    '''
    Solution w/o counter.
    Uses list of integers instead of dict.
    Indexes inside list is t-values of numbers.
    In the list zero empty values just for easier manipulation with indexes.    
    '''
    counter = [0 for item in range(1, 11)]
    score = 0

    for idx, item in enumerate(data):
        if item is not None:
            counter[item] += 1
    
    for t in range(1, 10):
        if counter[t] > 0 and k * 2 >= counter[t]:
            score +=1
    
    return score
    

if __name__ == '__main__':
    # start  = time.time()
    file_input = 'input.txt'
    file_output = 'output.txt'
    
    with open(file_input) as f:
        k = int(f.readline().rstrip())

        a = f.readline().rstrip()
        b = f.readline().rstrip()
        c = f.readline().rstrip()
        d = f.readline().rstrip()

        data = [
            *preprocess(a), 
            *preprocess(b), 
            *preprocess(c),
            *preprocess(d),
        ]
        solution = solve(k, data)
    
    with open(file_output, 'w') as f:
        f.write(str(solution))

    # end = time.time()
    # print(f'{(end - start)} seconds')
