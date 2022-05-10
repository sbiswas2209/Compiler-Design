productions = ["E=TD", "D=+TD", "D=#", "T=FS", "S=*FS", "S=#", "F=(E)", "F=a"]
lhs = ["E", "D", "T", "S", "F"]
l = ["E", "E'", "T", "T'", "F"]


def first(i):
    arr = []
    for j in productions:
        if i == j.split("=")[0] and i.isupper():
            if j.split("=")[1][0].isupper():
                arr += first(j.split("=")[1][0])
            else:
                arr.append(j.split("=")[1][0])
        elif not i.isupper():
            arr.append(i)
    return set(arr)


def follow(i):
    arr = []
    if i == "E":
        arr.append("$")
    for j in productions:
        try:
            idx = j.split("=")[1].index(i)
            length = len(j.split("=")[1])
            if idx == length - 1 and i != j.split("=")[0] and length >= 2:
                arr += follow(j.split("=")[0])
            elif idx < length - 1 and length > 2 and idx != 0:
                fir = first(j.split("=")[1][idx + 1])
                if "#" in fir:
                    arr += follow(j.split("=")[1][idx + 1])
                arr += fir
        except:
            continue
    arr = list(filter(lambda a: a != "#", arr))
    return set(arr)


for i in range(len(lhs)):
    print(f"First of {l[i]} =", first(lhs[i]))
    print(f"Follow of {l[i]} =", follow(lhs[i]))

