import pathlib
import json


file = pathlib.Path('json_line.txt')

data = [
    {'name': 'Telegram', 'type': 'messenger'},
    {'name': 'Instagram', 'type': 'social network'},
    {'name': 'VK', 'type': 'social network'},
    {'name': 'Viber', 'type': 'messenger'}
]

with file.open('w') as fd:
    dump = json.dumps(data, indent=4)
    fd.write(dump)

with file.open('r') as fd:
    dump = fd.read()
    l_date = json.loads(dump)
    print(l_date[3])
