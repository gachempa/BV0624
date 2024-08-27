# from variouys youtubes

def square_it(n):
    return n*n

x=[3,5,3,2,8,1]

y=list(map(square_it,x))
print(y)

def mu_len(n):
    return len(n)

x2 = map(mu_len, ("rock", "paper", "scissors"))

print(list(x2))
# people = [
#     {"name": "A", "age":1},
#     {"name": "D", "age":2},
#     {"name": "C", "age":3}
# ]

# people.sort(key=lambda person:person["name"])

# for p in people:
#     print(f"{p['name']}:{p['age']}")