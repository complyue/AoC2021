# %% # Part 1
cnt1478 = 0

with open("./input", "r") as f:
    for line in f:
        patterns, digits = line.strip().split("|")
        digits = digits.strip().split(" ")
        for d in digits:
            if len(d) in (2, 4, 3, 7):
                cnt1478 += 1

cnt1478

# %%
cipher = {
    "cf": 1,
    "acf": 7,
    "bcdf": 4,
    "acdeg": 2,
    "acdfg": 3,
    "abdfg": 5,
    "abcefg": 0,
    "abdefg": 6,
    "abcdfg": 9,
    "abcdefg": 8,
}

# %% # Part 2
sumall = 0

with open("./input", "r") as f:
    for line in f:
        patterns, digits = line.strip().split("|")
        patterns = sorted((set(dig) for dig in patterns.strip().split(" ")), key=len)
        digits = [set(dig) for dig in digits.strip().split(" ")]

        set_cf, set_acf, set_bcdf = patterns[:3]
        set_a = set_acf - set_cf
        set_bd = set_bcdf - set_acf
        for i in range(3, 9):
            patterns[i] -= set_a
        set_g = set.intersection(*patterns[3:9])
        for i in range(3, 9):
            patterns[i] -= set_g
        set_d = set.intersection(*patterns[3:6])
        set_b = set_bd - set_d
        set_cef = set.union(*patterns[3:6]) - set_b - set_d
        set_e = set_cef - set_bcdf
        for i in range(6, 9):
            patterns[i] = patterns[i] - set_b - set_d - set_e
        set_f = set.intersection(*patterns[6:9])
        set_c = set_cf - set_f

        transm = {
            tuple(*set_a)[0]: "a",
            tuple(*set_b)[0]: "b",
            tuple(*set_c)[0]: "c",
            tuple(*set_d)[0]: "d",
            tuple(*set_e)[0]: "e",
            tuple(*set_f)[0]: "f",
            tuple(*set_g)[0]: "g",
        }

        num = int(
            "".join(
                str(cipher["".join(sorted(transm[d] for d in ds))]) for ds in digits
            )
        )

        sumall += num

sumall

# %%
