# part 1
print(len(list(filter(lambda x: (x[0] <= x[2] <= x[3] <= x[1]) or (x[2] <= x[0] <= x[1] <= x[3]) ,[[int(x) for x in line.split('-')] for line in open('4.in').read().replace(',','-').split("\n")]))))
# part 2 
print(len(list(filter(lambda x: (x[0] <= x[2] <= x[1]) or (x[2] <= x[0] <= x[3]) or (x[2] <= x[1] <= x[3]) or (x[0] <= x[3] <= x[1]),[[int(x) for x in line.split('-')] for line in open('4.in').read().replace(',','-').split("\n")]))))
