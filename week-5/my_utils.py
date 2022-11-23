import sys
def average(values):
	""" Calculates the average of the given list. """
	total = 0;
	for n in values:        	# total the given values
		total += float(n) 
		average=total/len(values)  	 
	return average	# return calculated average
if __name__ == "__main__":
	print("The average is:" ,average(sys.argv[1:]))