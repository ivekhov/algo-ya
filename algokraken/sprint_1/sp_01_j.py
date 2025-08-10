import sys
import time
import math 

def solve_naive(num):
	a = num
	delimiter = 2
	result = []
	while a > 1:
		if a % delimiter == 0:
			a = a // delimiter
			result. append(str(delimiter))
			
		else:
			delimiter += 1
	return ' '.join(result)



def solve_naive_upd(num):
	if num == 2:
		return '2'
	a = num

	result = []
	
	for delimiter in range(2, int(math.sqrt(a)) + 1, 1):
		while a % delimiter == 0:
			result.append(str(delimiter))
			a = a // delimiter			
	if a > 2:
		result.append(str(a))
	return ' '.join(result)



def solve_speed(num):
	result = []
	while num % 2 == 0:
		result.append('2')
		num = num // 2
	
	for i in range(3, int(math.sqrt(num)) + 1, 2):
		while num % i == 0:
			result.append(str(i))
			num = num // i
	if num > 2:
		result.append(str(num))

	return ' '.join(result)


if __name__ == '__main__':
	num = int(sys.stdin.readline().rstrip())
	
	start = time.time()

	print(solve_naive_upd(num))	
	# print(solve_speed(num))
	# print(solve_naive(num))

	
	end = time.time()
	print(f'{(end - start) * 10*3}, ms')
	
	# 917521579

