import sys


def solve(sent):
	# get words
	words = sent.split(' ')
	# iterate finding max
	max_length = 0
	max_idx = 0
	for idx, item in enumerate(words):
		if len(item) > max_length:
			max_idx = idx
			max_length = len(item)

	return words[max_idx], max_length


if __name__ == '__main__':
	length = int(sys.stdin.readline().rstrip())
	sent = sys.stdin.readline().rstrip()
	solution = solve(sent)
	print(f'{solution[0]}\n{solution[1]}')

