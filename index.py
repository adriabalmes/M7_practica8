

# Opciones
options = ['selectall', 'insert', 'update', 'delete']

user_input = ''

input_message = "SELECT una opcion:\n"

for index, item in enumerate(options):
    input_message += f'{index+1}) {item}\n'

input_message += 'Has escojido: '

while user_input.lower() not in options:
    user_input = input(input_message)

# Selector del archivo python
if user_input == 'insert':
    print('Tu elecccion es: ' + user_input)
    exec(open("./insert.py").read())
elif user_input == 'update':
    print('Tu elecccion es: ' + user_input)
    exec(open("./update.py").read())
elif user_input == 'selectall':
    print('Tu elecccion es: ' + user_input)
    exec(open("./select.py").read())
else:
    print('Tu elecccion es: ' + user_input)
    exec(open("./delete.py").read())
