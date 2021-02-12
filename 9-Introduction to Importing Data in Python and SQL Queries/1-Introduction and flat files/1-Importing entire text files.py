file = open("moby_dick.txt", "r")
print(file.read())

print(file.closed)

file.close()
print(file.closed)
