print(max(sum(map(int, s.strip().split('\n'))) for s in open('1.in').read().split('\n\n')))
print(sum(sorted(sum(map(int, s.strip().split('\n'))) for s in open('1.in').read().split('\n\n'))[-3:]))