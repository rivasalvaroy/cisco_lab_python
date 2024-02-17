# Haciendo trampa con el metodo title()
def to_jaden_case(string):
    return string.title()


text_one = 'hola mundo, estoy aprendiendo python'
text_two = '  hola mundo, estoy aprendiendo python'
text_three = '1_hola mundo, 2estoy $aprendiendo  python'

print(to_jaden_case(text_one))
print(to_jaden_case(text_two))
print(to_jaden_case(text_three))
