import pathlib
import json


file = pathlib.Path('json_file.txt')

data = [
    {'name': 'Telegram', 'type': 'messenger'},
    {'name': 'Instagram', 'type': 'social network'},
    {'name': 'VK', 'type': 'social network'},
    {'name': 'Viber', 'type': 'messenger'}
]

with file.open('w') as fd:
    json.dump(data, fd, indent=4)

with file.open('r') as fd:
    l_date = json.load(fd)
    print(l_date)
