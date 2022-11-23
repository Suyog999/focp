import sys

count = len(sys.argv)
total = 0
if sys.argv[1:]==[]:
	print("no arguments were provided")
	exit()
else:
	while count > 1:
		count -= 1
		total += float(sys.argv[count])
average=float(total/len(sys.argv[1:]))
print("Total is", total)
print("Average is", average)