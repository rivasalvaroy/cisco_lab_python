# Reconstruyendo title() con capitalize() isalpha() and upper()
def to_jaden_case(string):
    aux = False
    text = ''

    if string[0].isalpha():
        string = string.capitalize()

    for i in string:
        if i == ' ' or not i.isalpha():
            aux = True
        elif aux == True:
            i = i.upper()
            aux = False
        text += i
    return text


text_one = 'hola mundo, estoy aprendiendo python'
text_two = '  hola mundo, estoy aprendiendo python'
text_three = '1_hola mundo, 2estoy $aprendiendo  python'

print(to_jaden_case(text_one))
print(to_jaden_case(text_two))
print(to_jaden_case(text_three))
