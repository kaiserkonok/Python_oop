# let's create an iterator of python

groceries = ['banana', 'orange', 'mango']

it = iter(groceries)

print(next(it))
print(next(it))
print(next(it))
# print(next(it))  # StopIteration Error


# let's create our own iterator

class Iterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def my_next(self):
        self.index -= 1
        if self.index < 0:
            raise StopIteration
        else:
            return self.data[self.index]


my_data = [1, 2, 3]

my_iterator = Iterator(my_data)

print(my_iterator.my_next())
print(my_iterator.my_next())
print(my_iterator.my_next())
