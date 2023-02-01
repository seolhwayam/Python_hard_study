a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
who=a,b,c
d=a
for i in who:
    if d>i:
        d=i
print(d)

