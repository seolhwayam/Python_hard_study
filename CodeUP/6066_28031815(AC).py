a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
who=a,b,c
for i in who:
    if i%2==0:
        print("even")
    else:
        print("odd")
        
