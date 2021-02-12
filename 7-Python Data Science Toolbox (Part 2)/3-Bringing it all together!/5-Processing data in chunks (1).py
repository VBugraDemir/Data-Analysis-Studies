with open("world_dev_ind.csv") as file:
    file.readline()
    counts_list = {}
    for j in range(1000):
        line = file.readline().split(",")

        first_col = line[0]
        if first_col in counts_list:
            counts_list[first_col] += 1
        else:
            counts_list[first_col] = 1
print(counts_list)