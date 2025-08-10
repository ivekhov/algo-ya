def __solution_1(arr, n):
	# corner cases, checks input quality ToDo
	
	res = []
	begin_idx = 0
	stop_idx = n
	
	for idx in range(len(arr) - n + 1):
		
		# calc
		ma_value = sum(arr[begin_idx:stop_idx]) / n
		res.append(ma_value)
		
		# change pointers
		begin_idx += 1
		stop_idx += 1
	
	
	return res


def __solution_2(arr, n):
	res = []
	for begin_idx in range(len(arr) - n + 1):
		end_idx = begin_idx + n
		ma = sum(arr[begin_idx:end_idx]) / n
		res.append(ma)
	return res


def solution(arr, n):
	res = []
	sum_items = sum(arr[0:n])
	res.append(sum_items / n)

	for begin_idx in range(0, len(arr) - n):
		end_idx = begin_idx + n
		sum_items -= arr[begin_idx]
		sum_items += arr[end_idx]
		res.append(sum_items / n)
	return res


if __name__ == '__main__':
	with open('input.txt', 'r') as f:
		n = f.readline().rstrip()
		arr = f.readline().rstrip()
		n = int(n)
		arr = list(map(int, arr.split(' ')))
		response = solution(arr, n)
	
	with open('output.txt', 'w') as f:
		f.write(' '.join(list(map(str, response))))

