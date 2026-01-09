import random as r
passw=""
new1=("a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,qr,s,t,u,v,w,x,y,z")
new2=("1,2,3,4,5,6,7,8,9")
new3=("!,@,#,$,%,&,*,?")
charac=new1.split(",")
num=new2.split(",")
special=new3.split(",")
fornum=int(input("enter the how many numbers"))
forchar=int(input("enter how many charc"))
forspe=int(input("enter how many special charac"))
for i in range(0,forchar):
    char=r.choice(charac)
    passw=passw+char
print(char)
for i in range(0,forspe):
    spe=r.choice(special)
    passw=passw+spe
for i in range(0,fornum):
    number=r.choice(num)
    passw=passw+number
print(passw)

