filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    
pi_string_v2 = ''
for line in lines:
    pi_string_v2 += line.strip()
    
print(pi_string_v2[:52] + '...')
print(len(pi_string_v2))

birthday = input('Enter your birthday, in the form mmddyy: ')
if birthday in pi_string_v2:
    print('Your birthday appears in the first million digits of pi!')
else:
    print('Your birthday does not appears in the first million digits of pi!')
