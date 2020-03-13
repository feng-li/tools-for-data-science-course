#I have learned some basic knowledge of python before
#Here is a simple review

m=int(input('平行四边形底为： '))
n=int(input('平行四边形高为： '))
while n>0:
    print(' '*(n-1)+'*'*m)
    n=n-1
    
    
def p(m,n):
    while n>0:
        print(' '*(n-1)+'*'*m)
        n=n-1

p(4,5)
