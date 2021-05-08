def ap():
    print("enter first term \n")
    a=float(input())
    print("enter common difference of progression \n")
    d=float(input())
    print("enter total number of terms in the progression \n")
    n=int(input())
    aplt=[]
    for i in range(n):
        t=a+i*d
        aplt.append(t)
    print(aplt)
    print("sum of terms in the progression = ",sum(aplt))



def gp():
    print("enter first term \n")
    a=float(input())
    print("enter the common ratio of progression \n")
    r=float(input())
    print("enter total number of terms in the progression \n")
    n = int(input())
    gplt = []
    for i in range(n):
        t = a*r**i
        gplt.append(t)
    print(gplt)
    print("sum of terms in the progression = ",sum(gplt))


def menu():
    print(" 1.CREATE ARITHEMATIC PROGRESSION OF YOUR CHOICE \n 2.CREATE GEOMETRIC PROGRESSION OF YOUR CHOICE \n 3.EXIT ")
    ch=int(input("enter the choice \n"))
    if ch==1:
        ap()
        menu()
    elif ch==2:
        gp()
        menu()
    elif ch==3:
        print("bye..")
        return
    else:
        print("enter valid choice \n")
        menu()
menu()
