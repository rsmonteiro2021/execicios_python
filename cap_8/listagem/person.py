# Devolvendo um dicionário

def build_person(first_name, last_name, age = ''):
    """Devolve um dicionário com informações sobre uma pessoa."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
musician = build_person('jimi', 'hendrix', age = 27)
print(musician)

# Inicialmente pensei em escrever o código dessa forma:
#def build_person(first_name, last_name, age = ''):
#    """Devolve um dicionário com informações sobre uma pessoa."""
    #if age:
    #    person = {'first': first_name, 'last': last_name, 'age': age}
    #else:
    #    person = {'first': first_name, 'last': last_name}
    #return person
#musician = build_person('jimi', 'hendrix')
#print(musician)
#musician = build_person('jimi', 'hendrix', age = 27)
#print(musician)