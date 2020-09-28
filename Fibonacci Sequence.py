#Fibonacci Sequence Challenge
def fibrec(n):
    if n <= 1:
        return n
    else:
        return fibrec(n-1) + fibrec(n-2)

def fib(n):
    for i in range(n):
        print(fibrec(i))

fib(5)
