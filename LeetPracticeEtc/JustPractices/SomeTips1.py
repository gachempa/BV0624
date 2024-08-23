# from variouys youtubes

people = [
    {"name": "A", "age":1},
    {"name": "D", "age":2},
    {"name": "C", "age":3}
]

people.sort(key=lambda person:person["name"])

for p in people:
    print(f"{p['name']}:{p['age']}")