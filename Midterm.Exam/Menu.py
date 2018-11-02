print("กรุณาเลือกเมนู : ")
print("กด 1 เพื่อหาพื้นที่วงกลม")
print("กด 2 เพื่อหาพื้นที่สามเหลี่ยม")
print("กด 3 ออกจากโปรแกรม")

print("==================&menu&===================");
while True :
    menu = int(input("เลือกเมนูที่ต้องการ : "))

    if menu == 1 :
        print("คำนวณหาพื้นที่ วงกลม")
        from Circle import *

    if menu == 2 :
        print("คำนวณหาพื้นที่สามเหลี่ยม")
        from Triangle import *

    if menu == 3 :
        print("ขอบคุณที่ใช้บริการ")
        break
    print("==================&menu&===================");
