import sys
import re

regex = re.compile('([\w.-]+)@([\w.-]+)')

with open(sys.argv[1], 'r') as f:
	for line in f:
		if line.strip() == '': continue
		if regex.match(line): print('true')
		else: print('false')
