from functools import reduce

stark = ['robb', 'sansa', 'arya', 'brandon', 'rickon']

result = reduce(lambda item1, item2: item1 + item2, stark)
print(result)