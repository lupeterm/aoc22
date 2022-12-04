# part 1
print(sum(map(lambda x: 1 if (x[0] <= x[2] <= x[3] <= x[1])   or (x[2] <= x[0] <= x[1] <= x[3])   else 0, [list(map(int, line.split('-'))) for line in open('4.in').read().replace(',','-').split("\n")])))
# part 2 
print(sum(map(lambda x: 1 if (x[0] <= (x[2] or x[3]) <= x[1]) or (x[2] <= (x[0] or x[1]) <= x[3]) else 0, [list(map(int, line.split('-'))) for line in open('4.in').read().replace(',','-').split("\n")])))
