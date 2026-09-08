heros = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']

# 1
print(f"Length of the list is: {len(heros)}")

# 2
heros.append("Black Panther")
print(heros)

# 3
heros.remove("Black Panther")
heros.insert(3, "Black Panther")
print(heros)

#4
heros[1:3] = ["Doctor Strange"]
print(heros)

#5
heros.sort()
print(heros)