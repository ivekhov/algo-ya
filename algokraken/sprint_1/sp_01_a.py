import sys


def solve(a, x, b, c):
    return a * x ** 2 + b * x + c


if __name__ == '__main__':
    nums = sys.stdin.readline().rstrip()
    nums = list(map(int, nums.split(' ')))
    # nums = [-8, -5, -2, 7]
    result = solve(nums[0], nums[1], nums[2], nums[3])
    # assert result == -183
    print(result)
    
    