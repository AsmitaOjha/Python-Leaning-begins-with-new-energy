a = 0
b = 1
n= int(input("Enter the nth fibonacci number: "))
if n<0:
    print("Enter positive intger")
elif n==1:
    print("Fibonacci number: 1")
else:
    print(a, end=",")
    for i in range(2,n):
        next_fibo = a+b
        print(next_fibo, end=",")
        #updating the value of a and b
        a,b = b, next_fibo
    print()
