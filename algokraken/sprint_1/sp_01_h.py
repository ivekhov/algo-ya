import sys


def bin2dec(word):
	result = []
	counter = len(word) - 1
	degree = 0
	while counter >= 0:
		result.append(int(word[counter]) * 2 ** degree)
		counter = counter - 1
		degree = degree + 1
	return sum(result)


def dec2bin(num):
	if num == 0:
		return '0'
	resid = num
	result = []
	while resid > 0:
		result.append(str(resid % 2))
		resid = resid // 2
	result.reverse()
	return ''.join(result)


if __name__ == '__main__':
	first = sys.stdin.readline().rstrip()
	second = sys.stdin.readline().rstrip()
	sum2 = bin2dec(first) + bin2dec(second)
	print(dec2bin(sum2))

