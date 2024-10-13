"""
You need to unpack N elements from an iterable, but the iterable may be longer than N
elements, causing a “too many values to unpack” exception
"""

# In this case the user has 2 numbers which needs to unpack
# data = ("Rana Fahad", 25, "344-567-234", "123-234-345")


# name, age, *numbers = data

# print(name)
# print(age)
# print(numbers)


# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# *trailing, last = my_list

# print()
# print(trailing)
# print(last)


records = [
('foo', 1, 2),
('bar', 'hello'),
('foo', 3, 4),
]


def foo(x, y):
    print('foo', x, y)
    
def bar(s):
    print('bar', s)
    
    
for tag, *args in records:
    if tag == 'foo':
        foo(*args)
    elif tag == 'bar':
        bar(*args)


