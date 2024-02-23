def persistence(n):
    counter = 0

    while len(str(n)) > 1:
        counter += 1
        aux = 1
        for i in str(n):
            aux *= int(i)
        n = aux
    else:
        return counter


print(persistence(39))
print(persistence(999))
print(persistence(4))
