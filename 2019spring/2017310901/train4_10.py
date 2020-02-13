import re
n=0
route='C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python36\\onl2.py'
with open (route,'r',encoding='utf-8') as f:
    for l in f:
        if re.match("for",l):
            n+=1
print(n)
