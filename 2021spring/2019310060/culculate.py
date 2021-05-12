count=1
output=0
a=1
b=2
while count<=1000:
    output=output*a
    c=a+b
    a=b
    b=c
    count=count+1
print(output)
