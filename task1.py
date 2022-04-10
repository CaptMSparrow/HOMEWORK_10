with open('lines.txt', 'w') as file:
    file.write('At 25 and still alive')

with open('lines.txt', 'r') as file:
    print(file.read())
