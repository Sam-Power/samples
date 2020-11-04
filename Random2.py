
"""

QUESTION:
This is an interview question asked by Amazon.
Given an array of numbers, find the maximum sum of any contiguous subarray of the array.
For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we
would take elements 42, 14, -5, and 86.
Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.

"""



arr = [34, -55, 34, 50, 42, 14, -5, 86]

def subseq(arr):
	i = len(arr)
	temp = 0
	lst = result = []
	while i:
		if sum(arr[:i]) > temp:
			temp = sum(arr[:i])
			lst = arr[:i]
		i-=1
	while i <  len(lst):
		if sum(lst[i:]) >= temp:
			temp = sum(lst[i:])
			result = lst[i:]

		i+=1
	if result == []:
		return 0
	return result
print(subseq(arr))