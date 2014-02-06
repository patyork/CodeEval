import sys

with open(sys.argv[1], 'r') as f:
	for line in f:
		a = 0
		b = 1
		found = False
		cycle = []
		seq = line.split()
		
		while not found:
			if seq[a] == seq[b]:
				endingPoint = b
				while b < len(seq) and seq[a] == seq[b] and a < endingPoint:
					cycle.append(seq[a])
					a += 1
					b += 1
				found = True
			else:
				b += 1
				if b >= len(seq):
					a += 1
					b = a + 1
		for one in cycle:
			print(one),
		print('')
