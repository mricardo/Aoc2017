def solve_maze(instrs):
    offset = 0
    steps = 0
    while(offset < len(instrs)):
        steps += 1
        new_offset = instrs[offset]
        instrs[offset] += 1
        offset = offset + new_offset

    return steps

instrs = list()
with open('input') as f:
    for i in f:
        instrs.append(int(i))

print(solve_maze(instrs))
