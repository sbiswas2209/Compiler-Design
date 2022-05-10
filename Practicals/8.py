grammar = {"E": ["E+T", "E-T", "T"], "T": ["T*F", "T/F", "F"], "F": ["(E)", "i"]}

variables = ["E", "T", "F"]
vals = ["+", "-", "*", "/", "(", ")", "i"]


def leading():
    lead = {x: list() for x in variables}
    for LHS in variables[::-1]:
        for RHS in grammar[LHS]:
            for char in RHS:
                if char in vals:
                    lead[LHS] += [char]
                    found = vals.index(char)
                    break

            for char in RHS[:found]:
                if char in variables and char != LHS:
                    lead[LHS] += lead[char]
                    break

    return lead


def trailing():
    trail = {x: list() for x in variables}
    for LHS in variables[::-1]:
        for RHS in grammar[LHS]:
            found = -1

            for char in RHS[::-1]:
                if char in vals:
                    trail[LHS] += [char]
                    found = vals.index(char)
                    break

            for char in RHS[(found + 1) :]:
                if char in variables and char != LHS:
                    trail[LHS] += trail[char]
                    break

    return trail


if __name__ == "__main__":
    lead = leading()
    for LHS in lead:
        print(f"LEADING({LHS}): {set(lead[LHS])}")

    print("/n")
    trail = trailing()
    for LHS in trail:
        print(f"TRAILING({LHS}): {set(trail[LHS])}")
