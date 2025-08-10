# https://contest.yandex.ru/contest/22450/run-report/134041699/

from collections import Counter


def preprocess(row):
    chars = [int(char) if char.isnumeric() else None for char in row ]
    return chars


def solve(k, data):
    counter = dict(Counter(data))
    score = 0

    for cycle in range(1, 10):
        if cycle in counter.keys():
            if k * 2 >= counter.get(cycle):
                score += 1
    
    return score



if __name__ == '__main__':
    FILENAME = 'input.txt'
    
    with open(FILENAME) as f:
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
    
    with open('output.txt', 'w') as f:
        f.write(str(solution))
