import sys

with open(sys.argv[1], 'r') as f:
	for line in f:
		sentence = line.split(', ')[0]
		replace = line.split(', ')[1].strip()
		for c in replace:
			sentence = str.replace(sentence, c, '')
		
		print sentence
