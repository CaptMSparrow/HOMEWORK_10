from pydantic import BaseModel


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


class Children(BaseModel):
    age: int
    name: str


class PersonalInform(BaseModel):
    age: int
    name: str
    children: list[Children]
    married: bool
    city: None


person = PersonalInform(**data)
print(person)
