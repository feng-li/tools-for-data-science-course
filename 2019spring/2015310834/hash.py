import re
start_hash = 0 
with open('新浪丢失儿童.py','r',encoding ='utf-8') as file:
    for line in file:
        if re.match('^#',line):
            start_hash += 1
print(start_hash)
