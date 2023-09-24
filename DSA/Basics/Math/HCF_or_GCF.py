a = 12
b = 6
L = []
for i in range(2, max(a, b)):
    if a % i == 0 and b % i == 0:
        L.append(i)
if L == []:
    print("no factors")
else:
    print(max(L))
