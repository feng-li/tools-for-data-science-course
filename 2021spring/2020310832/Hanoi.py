#Hanoi.py
x = eval(input())
count = 0
def hanoi(n, src='A', dst='B', mid='C'):
    global count
    if n == 1:
        print('{}:{}->{}'.format(1, src, dst))
        count += 1
    else:
        hanoi(n-1, src, mid, dst)
        print('{}:{}->{}'.format(n, src, dst))
        count += 1
        hanoi(n-1, mid, dst, src)
hanoi(x)
print(count)
