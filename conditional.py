a=5;
b=7;

if(a>b):
    print("A is greater than B");
elif(b>a):
    print("B is greater than A");
else:
    print("Both are equal");

if((30>20)and(20>30)):
    print("TRUE");
    for x in range(5):
        if(x==5):
            print(x);
else:
    print("Welcome");

#FRAME
for r in range(4):
    for c in range(4):
        if((r==0) or (r==3) or (c==0) or (c==3)):
            print("*",end="");
        else:
            print("",end=" ");
    print();