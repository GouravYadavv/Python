def print_subsequence(string, s2="", L: list = []):
    if string == "":
        L.append(s2)
        return L
    character = string[0]
    print_subsequence(string[1:], s2 + character, L)
    print_subsequence(string[1:], s2, L)
    return L


print(print_subsequence("abc"))
