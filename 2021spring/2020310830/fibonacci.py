def fib(n):
    a = [0,1]
    if n <= 2:
        return a[:n]
    for i in range(n-2):
        c = a[-1] + a[-2]
        a.append(c)

    return a


n = 1000


print(fib(n)

