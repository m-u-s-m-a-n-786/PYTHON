n=0
if n==0:
    print("0")
    print("1")

else:
    def fib(n):
        a=0
        b=1
        print(a)
        print(b)
        for i in range (2,n):
            c=a+b
            print(c)
            a=b
            b=c


fib(n=3)