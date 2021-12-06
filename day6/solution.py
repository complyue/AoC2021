# %% # Parse input
with open("./input", "r") as f:
    timers = [int(ns) for ns in f.readline().split(",")]
timers


# %%
def simulate(ndays=80):
    pace_groups = [0 for _ in range(7)]

    for t in timers:
        pace_groups[t] += 1

    i0, pg7, pg8 = 0, 0, 0
    for _ in range(ndays):

        borning = pace_groups[i0]
        pace_groups[i0] += pg7  # 0 to 6 plus 7 to 6
        pg7 = pg8
        pg8 = borning

        i0 = (i0 + 1) % 7

    return sum(pace_groups) + pg7 + pg8


# %% # Part 1
simulate()

# %% # Part 1
simulate(256)

# %%
