import sys

with open(sys.argv[1], 'r') as f:
	for line in f:
		split = line.strip().split(';')
		set1 = set(split[0].split(','))
		set2 = set(split[1].split(','))
		inter = list(set1.intersection(set2))
		inter.sort()
		print ','.join(item for item in inter)
