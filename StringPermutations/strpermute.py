import sys
import itertools

with open(sys.argv[1], 'r') as f:
	for line in f:
		chars = list(line.strip())
		out = []
		for perm in itertools.permutations(chars):
			permutation = ''
			for c in perm:
				permutation += c
			out.append(permutation)
		print ','.join(item for item in sorted(out))
			
