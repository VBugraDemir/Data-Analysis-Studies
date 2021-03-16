mutants = ('charles xavier',
 'bobby drake',
 'kurt wagner',
 'max eisenhardt',
 'kitty pryde')


powers = ('telepathy',
 'thermokinesis',
 'teleportation',
 'magnetokinesis',
 'intangibility')

z1 = zip(mutants, powers)

print(*z1)

z1 = zip(mutants, powers)

result1, result2 = zip(*z1)

print(result1 == mutants)
print(powers == result2)
