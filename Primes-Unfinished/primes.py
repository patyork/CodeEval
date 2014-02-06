import sys

with open(sys.argv[1], 'r') as f:
	for line in f:
		## apply the Sieve of Atkin
		
		results = [2, 3, 5]
		sieve = [i for i in range(6, int(line.strip()))]
		sieveRemainders = [i % 60 for i in range(6, int(line.strip()))]
		sieveStatus = [False for i in range(6, int(line.strip()))]
		
		for i in range(0, len(sieveRemainders)):
			if sieveRemainders[i] == 1 or sieveRemainders[i] == 13 or sieveRemainders[i] == 17 or sieveRemainders[i] == 29 or sieveRemainders[i] == 37 or sieveRemainders[i] == 41 or sieveRemainders[i] == 49 or sieveRemainders[i] == 53:
				print sieve[i],
