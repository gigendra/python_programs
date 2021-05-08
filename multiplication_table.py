def prdt():
    print("enter limit \n")
    a=int(input())
    print("_______MULTIPLICATION TABLE______ \n")
    for i in range(1,a+1,1):
        for j in range(1,11,1):
            p=i*j
            print("{} * {} = ".format(i,j),end='')
            print(p)
        print("\n")
prdt()