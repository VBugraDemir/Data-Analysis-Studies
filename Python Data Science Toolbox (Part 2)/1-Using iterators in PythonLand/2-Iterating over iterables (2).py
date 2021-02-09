# range() doesn't actually create a list; instead, it creates a
# range object with an iterator that produces the values until it reaches the limit

small_values = iter(range(3))
print(next(small_values))
print(next(small_values))
print(next(small_values))


for num in range(3):
    print(num)

googol = iter(range(10 ** 100))
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))
