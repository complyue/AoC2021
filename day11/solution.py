# %%
import numpy as np

# %% # Parse Input
with open("./input", "r") as f:
    input_ = np.array([list(line.strip()) for line in f.readlines()], dtype=int)


# %% # Part 1
energies = input_.copy()


def inc(i, j):
    if i < 0 or i >= energies.shape[0]:
        return
    if j < 0 or j >= energies.shape[1]:
        return
    if energies[i, j] == 0:
        return
    energies[i, j] += 1


def chk_flash(i, j):
    if energies[i, j] <= 9:
        return False

    energies[i, j] = 0

    inc(i - 1, j - 1)
    inc(i - 1, j)
    inc(i - 1, j + 1)
    inc(i, j - 1)
    inc(i, j + 1)
    inc(i + 1, j - 1)
    inc(i + 1, j)
    inc(i + 1, j + 1)

    return True


total_flashes = 0

for _ in range(100):
    energies[:] += 1
    step_flashes = 0
    while True:
        for i in range(energies.shape[0]):
            for j in range(energies.shape[1]):
                if chk_flash(i, j):
                    step_flashes += 1
        if step_flashes > 0:
            total_flashes += step_flashes
            step_flashes = 0
        else:
            break

total_flashes


# %% # Part 1
energies = input_.copy()


def inc(i, j):
    if i < 0 or i >= energies.shape[0]:
        return
    if j < 0 or j >= energies.shape[1]:
        return
    if energies[i, j] == 0:
        return
    energies[i, j] += 1


def chk_flash(i, j):
    if energies[i, j] <= 9:
        return False

    energies[i, j] = 0

    inc(i - 1, j - 1)
    inc(i - 1, j)
    inc(i - 1, j + 1)
    inc(i, j - 1)
    inc(i, j + 1)
    inc(i + 1, j - 1)
    inc(i + 1, j)
    inc(i + 1, j + 1)

    return True


step = 0
while True:
    step += 1
    energies[:] += 1
    step_flashes = 0
    while True:
        for i in range(energies.shape[0]):
            for j in range(energies.shape[1]):
                if chk_flash(i, j):
                    step_flashes += 1
        if step_flashes > 0:
            step_flashes = 0
        else:
            break
    if np.all(energies == 0):
        print(step)
        break

# %%
