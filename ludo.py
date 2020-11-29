import random
while(True):
    a=int(input("Press 1 For Playing LUDO & Any Key For Exit\n"))
    if(a!=1):
        print("Thanks For Playing LUDO")
        break
    while(a==1):
        s=random.randint(1,6)
        s=int(s)
        print(s)
        a+=1
