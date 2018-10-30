Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print('หาพื้นที่รูปวงกลม')
หาพื้นที่รูปวงกลม
>>> import math
>>> r = float(input("รัศมี:"))
รัศมี:
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    r = float(input("รัศมี:"))
ValueError: could not convert string to float: 
>>> r = float(input("รัศมี:"))
รัศมี:20
>>> a=math.pi*r**2
>>> print('พื้นที่วงกลม')
พื้นที่วงกลม
>>> 
>>> print('หาพื้นที่สามเหลี่ยม')
หาพื้นที่สามเหลี่ยม
>>> import math
>>> b = float(input("ฐาน:"))
ฐาน:60
>>> h = float(input("สูง"))
สูง120
>>> a =120/60*H*B
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a =120/60*H*B
NameError: name 'H' is not defined
>>> 
>>> a = 1/2*H*B
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    a = 1/2*H*B
NameError: name 'H' is not defined
>>> a=1/2*h*b
>>> print ('พื้นที่สามเหลี่ยม')
พื้นที่สามเหลี่ยม
>>> 160
160
>>> 
