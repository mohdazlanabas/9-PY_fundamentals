import json

person = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "hasChildren": False,
    "titles": ["Engineer", "Programmer"],
}

personJSON = json.dumps(person, indent=4, sort_keys=True)
print(personJSON)
with open("person.json", "w") as file:
    json.dump(person, file, indent=4)


person = json.loads(personJSON)
print(person)

with open("person.json", "r") as file:
    person = json.load(file)
print(person)


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


user = User("Max", 27)


def encode_user(o):
    if isinstance(o, User):
        return {"name": o.name, "age": o.age, o.__class__.__name__: True}
    else:
        raise TypeError("Object of type User is not JSON serializable")

    userJSON = json.dumps(user, default=encode_user)
    print(userJSON)
