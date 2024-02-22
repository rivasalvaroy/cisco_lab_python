def rot13(text):
    aux = ''
    for i in text:
        if i.isalpha():
            i = chr(ord(i) + 13)
            if i > 'z' or (i > 'Z' and chr(ord(i) - 13) <= 'Z'):
                i = chr(ord(i) - 26)
        aux += i
    return aux


text = 'hellO!, Hi5'
print(rot13(text))
