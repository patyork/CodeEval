import sys
import math

#Use golden ration instead of recursion
# Just an intersting interrelationship
gr = (1 + math.sqrt(5)) / 2

def Fib(x):
	return (pow(gr, x) - pow(1 - gr, x)) / math.sqrt(5)

with open(sys.argv[1], 'r') as f:
	for line in f:
		print(int(Fib(int(line.strip()))))
