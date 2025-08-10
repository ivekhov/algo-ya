import sys

def solve(sent):
	phrase = []
	for s in sent:
		if s not in " -`~()>@_!,.:?;*'":
			phrase.append(s)
	terms = ''.join(phrase)
	
	# regular expresson 
	# terms = ''.join(re.findall('[a-zA-Z]', sent))
	
	# simple with str method str.isalpha() == letters
	terms = ''.join([char for char in sent if char.isalpha()])	

	if terms[::-1] == terms[::]:
		return True
	return False


if __name__ == '__main__':
	sent = sys.stdin.readline().rstrip().lower()
	print(solve(sent))

