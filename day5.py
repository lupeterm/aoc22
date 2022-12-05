# part 1: 
boxes = [[list(map(lambda z: list(filter(lambda k: k != "", z)),list(zip(*map(lambda z: z.replace("] [", "-").replace("][", "-").replace("[", "").replace("]", "").replace(" ", "").split("-"),boxes.replace("    ", " [ ]").split("\n")[:-1],))),),),list(map(lambda f: list(map(int, f.split("-"))),rules.replace("move ", "").replace(" from ", "-").replace(" to ", "-").split("\n"),)),]for boxes, rules in [open("5.in").read().split("\n\n")]]
map(lambda BR: list(map(lambda r: exec(compile("boxes[0][0][r[2]-1] = list(reversed(boxes[0][0][r[1]-1][:r[0]:])) + boxes[0][0][r[2]-1]\nboxes[0][0][r[1]-1]=boxes[0][0][r[1]-1][r[0]:]","","exec")),BR[1])),boxes).__next__()
print("".join(zip(*boxes[0][0]).__next__()))
# part 2:
boxes = [[list(map(lambda z: list(filter(lambda k: k != "", z)),list(zip(*map(lambda z: z.replace("] [", "-").replace("][", "-").replace("[", "").replace("]", "").replace(" ", "").split("-"),boxes.replace("    ", " [ ]").split("\n")[:-1],))),),),list(map(lambda f: list(map(int, f.split("-"))),rules.replace("move ", "").replace(" from ", "-").replace(" to ", "-").split("\n"),)),]for boxes, rules in [open("5.in").read().split("\n\n")]]
map(lambda BR: list(map(lambda r: exec(compile("boxes[0][0][r[2]-1] = boxes[0][0][r[1]-1][:r[0]:] + boxes[0][0][r[2]-1]\nboxes[0][0][r[1]-1]=boxes[0][0][r[1]-1][r[0]:]","","exec")),BR[1])),boxes).__next__()
print("".join(zip(*boxes[0][0]).__next__()))
