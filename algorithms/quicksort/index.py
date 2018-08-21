# ----------------------------------------
#	Quicksort Implementation
#	written by: whoam123
#	
#	Github: https://github.com/wh0am123
#  
#	Created at: 19/08/2018
# ----------------------------------------
import optparse;
from array import *;

#
#	Function quicksort():
#		This function takes a numbers array
#		and sort it implementing the most popular
#		and powerful sorting algorithm, Quicksort
#

# Picking up a numbers array
def quicksort(numbers):

	if len(numbers) <= 1: # Check if Array has just one element
		return numbers # Return Element

	pivot = numbers[int(len(numbers) / 2)] # Set Pivot as the Array middle
	left = array('i', []) # Setting < pivot array
	right = array('i', []) # Setting > pivot array
	mid = array('i', []) # Setting = pivot array

	for x in numbers: # First for loop, setting in all the less-than-pivot numbers in left
		if x < pivot:
			left.append(int(x))

	for y in numbers: # Second Loop, Setting in all the great-than-pivot numbers in right
		if y > pivot:
			right.append(int(y))

	for z in numbers: # Third Loop, Setting in all the numbers equal to pivot
		if z == pivot:
			mid.append(int(z))

	return quicksort(left) + mid + quicksort(right) # Returning the plus of left, mid and right array
# 
#	Function main():
#		Created for set the program presentation and
#		Set a variable called 'result' like a quicksort
#		rutine with a numbers array parameter
#
def main():
	print('---------------------------------');
	print(' ');
	print('            QUICKSORT');
	print('            wh0am123');
	print(' ');
	print('---------------------------------');
	numbers = input('Write a Set of Numbers Separeted by Comas: ');
	array = numbers.split(',');
	result = quicksort(array)
	#for x in result:
	#	print(x)
	out = ''
	for r in result:
		out = out + str(r) + ','
	print('\n')
	print('//0x2c8d Output[ Result: '+ out + ' ]...')

# Calling the main() function as
if __name__ == '__main__':
	main()

