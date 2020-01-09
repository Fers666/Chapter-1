a,b,c=float(input()),float(input()),str(input())
if (c=='/' or c=='div' or c=='mod') and b==0 :
    print('Деление на 0!')
else :
    if c=='+' :
        print(a+b)
    elif c=="-" :
        print(a-b)
    else :
        if c=='/' :
            print(a/b)
        elif c=='*' :
            print(a*b)
        else :
            if c=='mod':
                print(a%b)
            elif c=='pow' :
                print(a**b)
            else :
                print(a//b)
