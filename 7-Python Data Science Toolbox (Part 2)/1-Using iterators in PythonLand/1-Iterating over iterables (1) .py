# iterable is an object that can return an iterator, while an iterator is an object that
# keeps state and produces the next value when you call next() on it.

flash = ['jay garrick', 'barry allen', 'wally west', 'bart allen']

for person in flash:
    print(person)
print()
# Create an iterator for flash: superhero
superhero = iter(flash)
print(next(superhero))
print(next(superhero))
print(next(superhero))
print(next(superhero))
