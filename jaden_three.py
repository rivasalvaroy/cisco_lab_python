# Solución mas común en la web, pero no cumple con title()
def to_jaden_case(string):
    return " ".join([w.capitalize() for w in string.split()])


text_one = 'hola mundo, estoy aprendiendo python'
text_two = '  hola mundo, estoy aprendiendo python'
text_three = '1_hola mundo, 2estoy $aprendiendo  python'

print(to_jaden_case(text_one))
print(to_jaden_case(text_two))
print(to_jaden_case(text_three))
