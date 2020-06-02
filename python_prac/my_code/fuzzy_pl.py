from fuzzywuzzy import fuzz, process 

# function to imput two things and get out the fuzzy wuzzy ratio 

def fuz(first ,*args):
	#rat = first
	# make this part an if else statement that uses the ratio or partial ratio that is the highest
	#for x in 
	
	ratio = fuzz.ratio(first, args)
	return ratio

