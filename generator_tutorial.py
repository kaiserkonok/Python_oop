data = [1, 2, 3]


def square_numbers(nums):
    for i in nums:
        yield i * i


my_nums = square_numbers(data)

# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))

for num in my_nums:
    print(num)
