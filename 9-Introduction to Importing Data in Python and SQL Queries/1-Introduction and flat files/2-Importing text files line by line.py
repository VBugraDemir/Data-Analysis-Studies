# with open concept of a context manager
# While still within this construct, the variable file will be bound to open('huck_finn.txt')
# *** Moby dict text file is a plain text file.

with open("moby_dick.txt", "r") as file:
    print(file.readline())
    print(file.readline())
    print(file.readline())
