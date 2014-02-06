import sys
import math

#Use golden ration instead of recursion
# Just an intersting interrelationship
gr = (1 + math.sqrt(5)) / 2

def Fib(x):
	if x == 0: return 0
	if x == 1: return 1
	if x == 2: return 1
	return Fib(x-1) + Fib(x-2)

with open(sys.argv[1], 'r') as f:
	for line in f:
		print(Fib(int(line.strip())))
