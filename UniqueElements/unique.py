import sys

with open(sys.argv[1], 'r') as f:
	for line in f:
		uniqueSet = set()
		print ','.join(str(item) for item in [x for x in line.strip().split(',') if x not in uniqueSet and not uniqueSet.add(x)])
		
