a=int(input("nota 1.="))
b=int(input("nota 2.="))
c=int(input("nota 3.="))
if c>8:
    print ("notele de azi:",a,",",b,",",c)
elif (((a>b) and (a>c)) or ((a>=c) and (a>=b))):
    print ( "nota de azi:",a)
elif (((b>a) and (b>c)) or ((b>=c) and(b>=a))):
    print ( "nota de azi:",b)
elif (((a>b) and (a>c)) or ((a>=c) and(a>=b))):
    print ( "nota de azi:",c)