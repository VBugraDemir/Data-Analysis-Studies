#  The function filter() offers a way to filter out elements from a list that don't satisfy certain criteria.

fellowship = ['frodo', 'samwise', 'merry', 'pippin', 'aragorn', 'boromir', 'legolas', 'gimli', 'gandalf']

result = map(lambda member: len(member)>6, fellowship)
result_list = list(result)
print(result_list)

result = filter(lambda member: len(member)>6, fellowship)
result_list = list(result)
print(result_list)
