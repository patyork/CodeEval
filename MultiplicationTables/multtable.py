for i in range(1,13):
	first = True
	row = [x * i for x in range(1,13)]
	for num in row:
		if first:
			print str(num),
			first = False
		else: print '%3s' % str(num),
		
	print('')
