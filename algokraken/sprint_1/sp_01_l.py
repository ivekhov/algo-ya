import sys
from collections import Counter


def solve(first, second):
    a = dict(Counter(first))
    b = dict(Counter(second))
    for k, v in b.items():
        if a.get(k) is None or v > a.get(k):
            return k
             

if __name__ == '__main__':
    first = sys.stdin.readline().rstrip()
    second = sys.stdin.readline().rstrip()
    
    print(solve(first, second))
