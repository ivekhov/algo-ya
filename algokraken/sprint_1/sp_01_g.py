import sys


def solve(num):
	# simple
	# return bin(num)[2:]
	
	# wo bin()
	if num == 0:
		return '0'
	res = []
	
	# iterating
	residual = num
	while residual > 0:
		res.append(str(residual % 2))
		residual = residual // 2
	res.reverse()
	return ''.join(res) 


if __name__ == '__main__':
	num = int(sys.stdin.readline().rstrip())
	print(solve(num))

