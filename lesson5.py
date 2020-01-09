f=str(input())
if f=='треугольник' :
    a,b,c=float(input()),float(input()),float(input())
    p=(a+b+c)/2
    print((p*(p-a)*(p-b)*(p-c))**(1/2))
else:
    if f=='прямоугольник' :
        a,b=float(input()),float(input())
        print(a*b)
    else :
        if f=='круг' :
            r=float(input())
            print(3.14*(r**2))