class calcs:

    def menus(self):
        print('______BASIC CALCULATOR________')
        print("""enter 1 for addition \nenter 2 for subtraction \nenter 3 for multliplication \nenter 4 for division \nenter 0 for exit""")
        a=int(input("enter option: "))
        if a==1:
            o1.adds()
        elif a==2:
            o1.subs()
        elif a==3:
            o1.muls()
        elif a==4:
            o1.divs()
        elif a==0:
            o1.contd()
        else:
            print("invalid option selected,select correct option: \n")
            o1.menus()

    def adds(self):
        print("enter two  integers\n")
        a = int(input())
        b = int(input())
        print("a+b=", a + b)
        o1.contd()
    def subs(self):
        print("enter two two  integers \n")
        a = int(input())
        b = int(input())
        print("a-b=", a - b)
        o1.contd()
    def muls(self):
        print("enter two  two  integers\n")
        a = int(input())
        b = int(input())
        print("a*b=", a * b)
        o1.contd()
    def divs(self):
        print("enter two  two  integers\n")
        a = int(input())
        b = int(input())
        print("a/b=", a / b)
        o1.contd()
    def contd(self):
        a=int(input("""to confirm exit enter 1\nto continue enter 2\n"""))
        if a==1:
            print("exit")
        elif a==2:
            o1.menus()
        else:
            print("invalid option, enter correct option: \n")
            o1.contd()

o1=calcs()
o1.menus()