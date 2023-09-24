def Print_Subset(up, p=""):
    if up == "":
        print(p)
        return
    Character = up[0]
    Print_Subset(up[1:], p + Character)
    Print_Subset(up[1:], p)


Print_Subset("abcd")
