'''Hanoi问题'''
def hanoi(n,Begin_Col,End_Col,Media_Col):
    if n==1:
        print(Begin_Col+'-->'+End_Col)
    else:
        hanoi(n-1,Begin_Col,Media_Col,End_Col)
        print(Begin_Col+'-->'+End_Col)
        hanoi(n-1,Media_Col,End_Col,Begin_Col)

n=int(input('请输入Hanoi塔的阶数：\t'))
hanoi(n,'A','B','C')

