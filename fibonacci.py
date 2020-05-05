# Fibonacci Series
# 0 1 1 2 3 5 8 13 21 34
def fibonacci_seq(n):
    a = 0               #first Number
    b = 1               #second Number
    if n == 1:
        print(a)
    elif n == 2:
        print(a,b)
    else:
        print(a,b, end = " ")
        for i in range(n-2):
            c = a + b
            a = b
            b = c
            print(c, end = " ")

fibonacci_seq(10)




