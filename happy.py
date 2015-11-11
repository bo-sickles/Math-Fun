import sys

def is_happy(number):
	#Determines whether a number is happy
	number = str(number)
	while len(number) > 1:
		number.split()
		result = 0
		for x in number:
			result += int(x) ** 2
		number = str(result)
	return int(number) == 1
	
if __name__ == "__main__":
	print is_happy(sys.argv[1])
