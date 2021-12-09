# %%
import numpy as np

# %% # Parse Input
with open("./input", "r") as f:
    input_ = np.array([list(line.strip()) for line in f.readlines()], dtype=int)


# %% # Part 1
def grads(i, j):
    if i > 0:
        yield input_[i, j] - input_[i - 1, j]
    if i < input_.shape[0] - 1:
        yield input_[i, j] - input_[i + 1, j]
    if j > 0:
        yield input_[i, j] - input_[i, j - 1]
    if j < input_.shape[1] - 1:
        yield input_[i, j] - input_[i, j + 1]


risk_sum = 0

for i in range(input_.shape[0]):
    for j in range(input_.shape[1]):
        if max(*grads(i, j)) < 0:
            risk_sum += 1 + input_[i, j]

risk_sum


# %% # Part 2
basins = np.zeros_like(input_)


def flow_down(i, j):
    h = input_[i, j]
    if h == 9:
        return
    if i > 0:
        if h - input_[i - 1, j] > 0:
            return flow_down(i - 1, j)
    if i < input_.shape[0] - 1:
        if h - input_[i + 1, j] > 0:
            return flow_down(i + 1, j)
    if j > 0:
        if h - input_[i, j - 1] > 0:
            return flow_down(i, j - 1)
    if j < input_.shape[1] - 1:
        if h - input_[i, j + 1] > 0:
            return flow_down(i, j + 1)
    basins[i, j] += 1


for i in range(input_.shape[0]):
    for j in range(input_.shape[1]):
        flow_down(i, j)

np.prod(np.sort(basins.flat)[-3:])

# %%
