print(range (10))

for i in range (10):
    print(i)

def fibonacci(max) :
    a, b = 0,1
    while a < max:
        yield a
        a, b = b, a+b

fib1 = fibonacci(20)

fib_nums = [num for num in fib1]


