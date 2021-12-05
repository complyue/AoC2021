# %%
import re

p = re.compile("([0-9]+),([0-9]+) -> ([0-9]+),([0-9]+)")


# %% # Part 1
mark_cnts = {}

with open("./input", "r") as f:
    for line in f:
        x1, y1, x2, y2 = (int(ns) for ns in p.match(line).groups())
        if x1 == x2:
            step = y2 > y1 and 1 or -1
            for y in range(y1, y2 + step, step):
                key = x1, y
                mark_cnts[key] = 1 + mark_cnts.get(key, 0)
        elif y1 == y2:
            step = x2 > x1 and 1 or -1
            for x in range(x1, x2 + step, step):
                key = x, y1
                mark_cnts[key] = 1 + mark_cnts.get(key, 0)
        else:
            pass

sum(1 for c in mark_cnts.values() if c > 1)


# %% # Part 2
mark_cnts = {}

with open("./input", "r") as f:
    for line in f:
        x1, y1, x2, y2 = (int(ns) for ns in p.match(line).groups())
        if x1 == x2:
            step = y2 > y1 and 1 or -1
            for y in range(y1, y2 + step, step):
                key = x1, y
                mark_cnts[key] = 1 + mark_cnts.get(key, 0)
        elif y1 == y2:
            step = x2 > x1 and 1 or -1
            for x in range(x1, x2 + step, step):
                key = x, y1
                mark_cnts[key] = 1 + mark_cnts.get(key, 0)
        else:
            step_x = x2 > x1 and 1 or -1
            step_y = y2 > y1 and 1 or -1
            for x, y in zip(
                range(x1, x2 + step_x, step_x), range(y1, y2 + step_y, step_y)
            ):
                key = x, y
                mark_cnts[key] = 1 + mark_cnts.get(key, 0)

sum(1 for c in mark_cnts.values() if c > 1)

# %%
