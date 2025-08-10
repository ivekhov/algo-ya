import sys


def solve(matrix, row, col):
	if row < 0 or col < 0:
		return ''
	if row > len(matrix):
		return ''
	if col > len(matrix[0]):
		return ''

	result = []
	if (col - 1) >= 0:
		result.append(matrix[row][col-1])
	if (col + 1) < len(matrix[row]):
		result.append(matrix[row][col+1])
	if (row - 1) >= 0:
		result.append(matrix[row-1][col])
	if (row + 1) < len(matrix):
		result.append(matrix[row+1][col])
	result.sort()
	return ' '.join(list(map(str, result)))



if __name__ == '__main__':
	height = sys.stdin.readline().rstrip()
	width = sys.stdin.readline().rstrip()
	matrix = []
	for i in range(int(height)):
		row = sys.stdin.readline().rstrip().split(' ')
		matrix.append(list(map(int, row)))
	row = int(sys.stdin.readline().rstrip())
	col = int(sys.stdin.readline().rstrip())


	solution = solve(matrix, row, col)
	print(solution)

