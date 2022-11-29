import glob
from cffi.setuptools_ext import execfile


options = ['insert', 'update', 'delete']

user_input = ''

input_message = "SELECT una opcion:\n"

for index, item in enumerate(options):
    input_message += f'{index+1}) {item}\n'

input_message += 'Has escojido: '

while user_input.lower() not in options:
    user_input = input(input_message)


if user_input == 'insert':
    print('Tu elecccion es: ' + user_input)
    execfile('insert.py')
elif user_input == 'update':
    print('Tu elecccion es: ' + user_input)
    execfile('update.py')
else:
    print('Tu elecccion es: ' + user_input)
    execfile('delete.py')




