# Generator functions are functions that, like generator expressions, yield a series of values, instead
# of returning a single value.

lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']

def get_lengths(input_list):
    for name in input_list:
        yield len(name)

for value in get_lengths(lannister):
    print(value)
