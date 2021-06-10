# let's create an iterator of python

groceries = ['banana', 'orange', 'mango']

it = iter(groceries)

print(next(it))
print(next(it))
print(next(it))
print(next(it))  # StopIteration Error
