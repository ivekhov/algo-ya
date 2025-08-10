import sys
import time


def solve(temp):
	# create list with this days
	if len(temp) == 1:
		return 1
	
	# result = []
	counter = 0
	for idx, item in enumerate(temp):
		if idx == 0:
			if item > temp[idx+1]:
				counter = counter + 1
				# result.append(item)
		elif idx == len(temp) - 1:
			if item > temp[idx-1]:
				counter = counter + 1
				# result.append(item)
		else:
			if item > temp[idx-1] and item > temp[idx+1]:
				counter = counter + 1
				# result.append(item)
	return counter
	# return len(result)
	


if __name__ == '__main__':
	start_time = time.time()
	days = int(sys.stdin.readline().rstrip())
	row = sys.stdin.readline().rstrip().split(' ')
	temp = list(map(int, row))
	print(solve(temp)) 

	# print("The time of execution of above program is :", (time.time() - start_time) * 10**3, "ms")

