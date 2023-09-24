a = ord("A")
for i in range(5):
    for j in range(i + 1):
        print(chr(a), end=" ")
        a = ord(chr(a)) + 1
    print()
