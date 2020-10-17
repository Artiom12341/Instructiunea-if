a=int(input("b.alb M="))
b=int(input("b.rosii M.="))
c=int(input("b. verzi M.="))
d=int(input("b. albe m.="))
e=int(input("b.rosii m.="))
f=int(input("b.verzi m.="))
print("bile in total=", a+b+c+d+e+f)
if (a+b+c)>(d+e+f):
    print("bile mari=",a+b+c)
elif (a+b+c)<(d+e+f):
    print("bile mici=",d+e+f)

if (((a+d)>(b+e)) and ((a+d)>(b+e))):
    print("bile albe=",a+d)
elif (((b+e)>(a+d)) and ((c+f)<(b+e))):
    print("bile rosii=",b+e)
elif (((c+f)>(b+e)) and ((a+d)<(c+f))):
    print("bile verzi=",c+f)