from re import match
Hash_Start = 0
with open('L2.py', 'r') as file:
    for line in file:
        if match("#", line):
            Hash_Start += 1
print(Hash_Start)
