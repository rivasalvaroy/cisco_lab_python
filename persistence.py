def persistence(n):
    n = str(n)

    if len(n) == 1:
        return print(0)

    while len(n) > 1:
        aux = 1
        for i in n:
            aux *= int(i)
        n = str(aux)
    else:
        print(n)


persistence(39)
persistence(999)
persistence(4)
