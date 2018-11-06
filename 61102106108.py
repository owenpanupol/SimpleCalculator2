print("find the geometry area : ")
print("push1 find a circle area")
print("push2 find a triangle area")
print("exit")

print(".............&menu&.............");
while True :
    menu = int(input("number : "))

    if menu == 1 :
        print("find a circle area")
        import math
        r = float(input("cost number ."))
        AREA = 3.14*r**2
        print('circle area = ', AREA) 

    if menu == 2 :
        print("find a triangle area")
        import math
        B = float(input("Please enter a length value"))
        H = float(input("Please enter a height value"))
        A = 1/2*H*B
        print("triangle area = %.2f" % A)

    if menu == 3 :
        print("big thanks")
        break
    print(".............&menu.............&");
