L = [68, 70, 56, 60, 71, 72, 80, 40, 74]

min_value = []

L = sorted(L)

for i in range(len(L)):
    if L[i] % 10 == 0:
        min_value.append(L[i])


print(min_value[:3])