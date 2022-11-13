a=300
b=600
i=1
ss=0

while b>=a:
    while i<=a:
        if (a%i==0):
            ss+=i
        i+=1
    if (ss%1==0):
        print(ss,end=' ')
        print(a)
    a+=1
        
