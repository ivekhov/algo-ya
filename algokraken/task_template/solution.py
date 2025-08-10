def solution():
	pass


def main(input_file='input.txt', output_file='output.txt'):
	with open(input_file, 'r') as f:
		n = int(f.readline().rstrip())
		commands = f.readline().rstrip().split(' ')
		
		for _ in range(n):
			pass
	
	
	res = solution()
	
	with open(output_file, 'w') as f_out:
		f_out.write(f'{str(res)}\n')


if __name__ == '__main__':
	fixtures =[
        ['input.txt', 'output.txt'],

		# comment below before submit to Contest Checker:
        # ['input_2.txt', 'output_2.txt'],
        # ['input_3.txt', 'output_3.txt'],
    ]
	for fixture in fixtures:
		main(fixture[0], fixture[1])