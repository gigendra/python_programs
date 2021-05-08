class schoo:
    __age=None
    __name=None
    __ph=None
    __sal=None
    __com=None

    def reads(self):
        print("enter name of employee (maximum of 15 chaaracters)\n")
        a=input()
        if len(a)>15:
            n2=len(a)
            while(n2>15):
                 print("re-enter name of employeee (maximum of 15 chaaracters) \n")
                 a=input()
                 n2=len(a)
        self.__name=a
        print("enter age of employee \n")
        b = int(input())
        while(b > 60 or b < 18):
                print("enter a valid age \n")
                b=int(input())
        b1=str(b)
        self.__age = b1
        print("enter phone number of employee (10 digits )\n")
        c = int(input())
        c1=str(c)
        if len(c1)!=10:
            n1=len(c1)
            while(n1!=10):
                print("enter a 10 digit phone number")
                c = int(input())
                c1 = str(c)
                n1=len(c1)
        self.__ph = c1
        print("enter salary of employee \n")
        d=input()
        self.__sal = d
        print("enter company name (maximum 10 characters)\n")
        e = input()
        if len(e)>10:
            n3=len(e)
            while(n3>10):
                print("enter company name (maximum 10 characters)\n")
                e = input()
                n3=len(e)
        self.__com = e

    def filesr(self):
        f=open("emps.txt","a")
        line=[self.__name,self.__age,self.__ph,self.__sal,self.__com]
        for l in line:
            f.write(l)
            f.write(" --- ")

        f.write("\n")
        f.close()
    def filesp(self):
        f=open("emps.txt", "r")
        print(f.read())


n = int(input("enter the no.of employees"))
for i in range(n):
    o = schoo()
    o.reads()
    o.filesr()
o.filesp()



