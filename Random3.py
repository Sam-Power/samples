"""
QUESTION:
This is an interview question asked by Facebook.

Given a array of numbers representing the stock prices of a company in
chronological order, write a function that calculates the maximum profit
you could have made from buying and selling that stock once. You must buy
before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you
could buy the stock at 5 dollars and sell it at 10 dollars.

"""
lst = [10, 9, 11, 8, 5, 7, 10]
profit=0
j = lst[0]
for i in lst:
	if i < j:
		j = i
	if i - j > profit:
		profit = i - j
print(profit)

lst = [9, 11, 8, 5, 7, 10]
maxdif = 0
for i in range(len(lst)):
	for y in range(len(lst)):
		if lst[y]-lst[i] > maxdif and y > i:
			maxdif = lst[y]-lst[i]
print(maxdif)