"""
    Finding the N largest or smallest numbers in a collection.

"""

import heapq


my_collection = [1, 65, 3, -8, -5, 34, 9, 3, 56, 100, -23.66, -23, 20, 30, 300]


print(heapq.nlargest(4, my_collection))
print(heapq.nsmallest(4, my_collection))


portfolio = [
{'name': 'IBM', 'shares': 100, 'price': 91.1},
{'name': 'AAPL', 'shares': 50, 'price': 543.22},
{'name': 'FB', 'shares': 200, 'price': 21.09},
{'name': 'HPQ', 'shares': 35, 'price': 31.75},
{'name': 'YHOO', 'shares': 45, 'price': 16.35},
{'name': 'ACME', 'shares': 75, 'price': 115.65}
]

print("\n-------------------------------------\n")

print(heapq.nlargest(3, portfolio, key=lambda s:s['price']))
print(heapq.nsmallest(3, portfolio, key=lambda s:s['price']))
