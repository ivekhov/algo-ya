import sys


def solve(num):
	residual = num
	while residual > 1:
		residual = residual / 4
	if residual == 1:
		return True
	return False


if __name__ == '__main__':
	num = int(sys.stdin.readline().rstrip())
	print(solve(num))

