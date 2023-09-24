def SubSets_with_ASCAII_value(string: str, p=""):
    if string == "":
        print(p)
        return
    ch: str = string[0]
    SubSets_with_ASCAII_value(string[1:], p)
    SubSets_with_ASCAII_value(string[1:], p + ch)
    SubSets_with_ASCAII_value(string[1:], p + ord(ch))


SubSets_with_ASCAII_value("abc")
