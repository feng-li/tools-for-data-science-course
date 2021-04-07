class Fibonacci(object):
    '''斐波那契数列迭代器'''
    
    def __init__(self, n):
        self.n = n
        self.current = 0
        self.a = 0
        self.b = 1
    def __next__(self):
        if self.current < self.n:
            self.a, self.b = self.b, self.a + self.b
            self.current += 1
            return self.a
        else:
            raise StopIteration
   def __iter__(self):
       return self
if __name__ == '__main__':
    fib = Fibonacci(1000)
    
    for num in fib:
        print(num)
