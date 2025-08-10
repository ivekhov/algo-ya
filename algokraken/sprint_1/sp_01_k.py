import sys


def solve(list_form, k):
    nums = list_form.replace(' ', '')
    first = int(nums)
    second = int(str(k).replace(' ', ''))
    sum_ = first + second
    return ' '.join([char for char in str(sum_)])

if __name__ == '__main__':
    count = int(sys.stdin.readline().rstrip())
    list_form = sys.stdin.readline().rstrip()
    k = int(sys.stdin.readline().rstrip())
    print(solve(list_form, k))	

