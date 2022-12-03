#part 1
print(sum(map(lambda x: x - 96 if x > 90 else x - 38, [ord((set(line[: len(line) // 2]) & set(line[len(line) // 2 :])).pop()) for line in open('3.in').readlines()])))
# part 2 with numpy ...
import numpy as np
print(sum(map(lambda x: x - 96 if x > 90 else x - 38,[ord((set(x) & set(y) & set(z)).pop()) for x,y,z in np.loadtxt('3.in', dtype=str).reshape(-1,3)])))
# ... or without numpy:
print(sum(map(lambda x:x - 96 if x > 90 else x - 38 ,[ord((set(x.strip()) & set(y.strip()) & set(z.strip())).pop()) for x,y,z in [open('3.in').readlines()[x:x+3] for x in range(0, 300, 3)]])))