print("Please Select Menu : ")
print("Dail 1 Calcute area Circle")
print("Dial 2 Calcute area Triangle")
print("Dial 3 Exit program")

print("==================&menu&===================");
while True :
    menu = int(input("Select Menu : "))

    if menu == 1 :
        print("Calcute area Circle")
        from Circle import *

    if menu == 2 :
        print("Calcute area Triangle")
        from Triangle import *

    if menu == 3 :
        print("Thank you very much")
        break
    print("==================&menu&===================");



