options = ['select', 'update', 'delete']

user_input = ''

input_message = "SELECT una opcion:\n"

for index, item in enumerate(options):
    input_message += f'{index+1}) {item}\n'

input_message += 'Has escojido: '

while user_input.lower() not in options:
    user_input = input(input_message)

print('Tu elecccion es: ' + user_input)