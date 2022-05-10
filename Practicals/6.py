t = {"+", "*", "$", "a", "(", ")"}
nt = ["E", "D", "T", "S", "F"]
pror = {
    "E": ["TD"],
    "D": ["+TD", "#"],
    "T": ["FS"],
    "S": ["*FS", "#"],
    "F": ["(E)", "a"],
}
first = {
    "E": ["(", "a"],
    "D": ["+", "#"],
    "T": ["(", "a"],
    "S": ["*", "#"],
    "F": ["(", "a"],
}
follow = {
    "E": ["$", ")"],
    "D": ["$", ")"],
    "T": ["+", "$", ")"],
    "S": ["+", "$", ")"],
    "F": ["*", "+", "$", ")"],
}


for i in t:
    print(i, end="\t")
    for j in nt:
        fir = first[j]
        if "#" in fir:
            fir += follow[j]
        fir = list(filter(lambda a: a != "#", fir))
        if i in fir:
            flag = 0
            for k in pror[j]:
                if i in k:
                    print(f"{j}->{k}", end="\t")
                    flag += 1
                    break
                elif i not in k and "#" in k:
                    print(f"{j}->#", end="\t")
                    flag += 1
            if flag == 0:
                print(f"{j}->{pror[j][0]}", end="\t")
        else:
            print("", end="\t")
    print()

