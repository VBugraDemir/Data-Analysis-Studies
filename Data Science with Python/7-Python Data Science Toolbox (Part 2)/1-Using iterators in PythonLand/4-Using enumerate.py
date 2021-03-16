# returns an enumerate object that produces a sequence of tuples, and each of the tuples is an index-value pair.

mutants = ['charles xavier',
            'bobby drake',
            'kurt wagner',
            'max eisenhardt',
            'kitty pryde']

mutants_enm = list(enumerate(mutants))
print(mutants_enm)

for index1, value1 in enumerate(mutants):
    print(index1, value1)
print()
for index2, value2 in enumerate(mutants, start=1):
    print(index2, value2)
