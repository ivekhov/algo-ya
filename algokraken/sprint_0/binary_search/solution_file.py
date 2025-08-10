def solution(x, y):
	return x * y


if __name__ == '__main__':
	with open('input.txt', 'r') as f:
		first = f.readline().rstrip()
		second = f.readline().rstrip()
		row = f.readline().rstrip()
		nums = list(map(int, row.split(' ')))
		response = solution(int(first), int(second))
	
	with open('output.txt', 'w') as f:
		f.write(str(response))
