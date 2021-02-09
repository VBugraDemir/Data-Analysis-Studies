fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

new_fellowship = [member for member in fellowship if len(member)>=7]
print(new_fellowship)

# if else
new_fellowship = [member if len(member)>=7 else "" for member in fellowship]
print(new_fellowship)
