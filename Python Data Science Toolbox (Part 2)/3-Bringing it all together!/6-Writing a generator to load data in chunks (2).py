# Generators allow users to lazily evaluate data. This concept of lazy evaluation is useful
# when you have to deal with very large datasets because it lets you generate values in an efficient manner
# by yielding only chunks of data at a time instead of the whole thing at once.

def read_large_file(file_object):
    while True:
        data = file_object.readline()
        if not data:
            break
        yield data
with open("world_dev_ind.csv") as file:
    gen_file = read_large_file(file)

    print(next(gen_file))
    print(next(gen_file))
    print(next(gen_file))

