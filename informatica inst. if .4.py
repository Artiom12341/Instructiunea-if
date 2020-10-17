a=int(input("anul nas.="))
b=int(input("luna nas.="))
c=int(input("ziua nas.="))
d=int(input("anul cur.="))
e=int(input("luna cur.="))
f=int(input("ziua cur.="))

if ((f-c==0) and (e-b==0)) :
    print("varsta=",d-a)
elif ((f-c>0) and (e-b==0)):
    print("varsta=",d-a-1)
elif ((f-c<0) and (e-b==0)):
     print("varsta=",d-a)

elif ((f-c==0) and (e-b>0)) :
    print("varsta=",d-a)
elif ((f-c>0) and (e-b>0)):
    print("varsta=",d-a)
elif ((f-c<0) and (e-b>0)):
     print("varsta=",d-a)

elif ((f-c==0) and (e-b<0)) :
    print("varsta=",d-a-1)
elif ((f-c>0) and (e-b<0)):
    print("varsta=",d-a-1)
elif ((f-c<0) and (e-b<0)):
     print("varsta=",d-a-1)





