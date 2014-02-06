import sys
import re

regex = re.compile('\d+, \d+')

with open(sys.argv[1], 'r') as f:
	for line in f:
		print line
		output = regex.findall(line)
		print output
