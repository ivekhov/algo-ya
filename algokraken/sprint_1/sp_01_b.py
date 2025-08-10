import sys


def is_even(n):
    return True if n % 2 == 0 else False


def solve(nums):
    nums = nums.split(' ')
    nums = list(map(int, nums))

    res = sum(list(map(is_even, nums)))

    if res == 0:
    	return 'WIN'
    elif res == 3:
    	return 'WIN'
    return 'FAIL'


if __name__ == '__main__':
    # for local test
    # assert solve('1 2 -3') == 'FAIL'
    # assert solve('7 11 7') == 'WIN'
    # assert solve('6 -2 0') == 'WIN'
    
    # for contest
    nums = sys.stdin.readline().rstrip()
    print(solve(nums))
    