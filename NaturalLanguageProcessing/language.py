#Natural Language Processing - English to numerals
import sys

NEGATIVE = 'negative'

translations = dict(zero=0, one=1, two=2, three=3, four=4, five=5, six=6, seven=7, eight=8, nine=9,
    ten=10, eleven=11, twelve=12, thirteen=13, fourteen=14, fifteen=15, sixteen=16, seventeen=17, eighteen=18, nineteen=19,
	twenty=20, thirty=30, forty=40, fifty=50, sixty=60, seventy=70, eighty=80, ninety=90)
	
multipliers = dict(hundred=100, thousand=1000, million=1000000)
	


def translate(line):
	words = line.strip().split()
	
	negative = False
	output = 0
	i = 0
	while i < len(words):
		tmp = translations.get(words[i], 0)		#the first word will be a translation or will be the negative quantifier
		
		if words[i] == NEGATIVE:					#if NEGATIVE, set the flag, set tmp to 0
			negative = True
			tmp = 0
	
		elif i+1<len(words) and multipliers.get(words[i+1], -1) != -1:		#if there is another word and it is a multiplier
			i += 1
			tmp *= multipliers[words[i]]									#..then multiply it
			
			#Check for additional multipliers > the current one
			for j in range(i+1, len(words)):
			    if multipliers.get(words[j], -1) > multipliers[words[i]]:
			        
			        #check for additional cardinal numbers between here and there
			        if j > i+1: #if a word between here and the multipler
			            k = i+1
			            while k < j:
			                tmp += translations.get(words[k], 0)
			                k += 1
			        
			        # apply the upper multiplier
			        tmp *= multipliers.get(words[j], -1)
			        i = j # will move the parent loop past the multiplier
			        #j = len(words)  #break out
			        break
		elif i+2<len(words) and multipliers.get(words[i+2], -1) != -1:	#if the next is not a multiplier, but there is a next and the one after is amultiplier
			tmp += translations.get(words[i+1], 0)
			tmp *= multipliers[words[i+2]]
			i += 2
					
			
			
		output += tmp								#add what we have to the running total
		i += 1
	
	return -1 * output if negative else output
	

#Main program
with open(sys.argv[1], 'r') as f:
	for line in f:
		print translate(line)


#with open(sys.argv[1], 'r') as f:
#	wrongCount = 0
#	for line in f:
#		tests = line.strip().split('|')
#		if str(translate(tests[0])) != tests[1]:
#			print '%s translated to %i, should have been %s' % (tests[0], translate(tests[0]), tests[1])
#			wrongCount += 1
#	
#	print '\n\nWrong Count: %i' % wrongCount
		
		
		
		
		
		
		
		
		
		
