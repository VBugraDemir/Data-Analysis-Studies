# Another interesting function is zip(),
# which takes any number of iterables and returns a zip object that is an iterator of tuples.
# If you wanted to print the values of a zip object, you can convert it into a list and then print it.

mutants = ['charles xavier',
 'bobby drake',
 'kurt wagner',
 'max eisenhardt',
 'kitty pryde']

aliases = ['prof x', 'iceman', 'nightcrawler', 'magneto', 'shadowcat']

powers =['telepathy',
 'thermokinesis',
 'teleportation',
 'magnetokinesis',
 'intangibility']

mutant_data = list(zip(mutants, aliases, powers))
print(mutant_data)

mutant_zip = zip(mutants, aliases, powers)

for value1, value2, value3 in mutant_zip:
    print(value1, value2, value3)
