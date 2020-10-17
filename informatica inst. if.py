a=int(input("elev nr.1="))
b=int(input("elev nr.2="))
c=int(input("elev nr.3="))
d=int(input("scor nr.1="))
e=int(input("scor nr.2="))
f=int(input("scor nr.3="))
if ((d>e)and(d>f)):
    print("Scor max. la elevul",a,"=",d)
if ((e>d)and(e>f)):
    print("Scor max. la elevul",b,"=",e)
if ((f>d)and(f>e)):
    print("Scor max. la elevul",c,"=",f)
if d==e:
    print("Scor max. la elevii",a,",",b,"=",d)
if d==f:
    print("Scor max. la elevii",a,",",c,"=",d)
if e==f:
    print("Scor max. la elevii",b,",",c,"=",e)
if ((d==e) and (e==f)):
    print (" toti au scor egal = ",d)
