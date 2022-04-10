import pandas as pd


data = {
    'age': 45,
    'name': 'Peter',
    'children': [
        {
            'age': 3,
            'name': 'Alice'
        }
    ],
    'married': True,
    'city': None
}


def fdict(d):
    f_dict = pd.json_normalize(data, 'children').to_dict(orient='records')
    return f_dict


f = fdict(data)
print(*f)
