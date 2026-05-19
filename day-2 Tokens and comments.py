Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
num = 10
res = num + 5
print(res)
15
my number = 123
SyntaxError: invalid syntax
#num
num1 = 10
num2 = 20
num3 = 30
>>> num1 = 10,num2 = 20,num3 = 30
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
>>> num1,num2,num3 = 10,20,30
>>> print(num1)
10
>>> print(num2)
20
>>> print(num3)
30
>>> num1 = num2 = 10
>>> print(num1, num2)
10 10
>>> a = 10
>>> b = 20
>>> del a
>>> c = a + b
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    c = a + b
NameError: name 'a' is not defined
>>> n1 = n2 = n3 = 15
>>> del n2
>>> print(n3)
15
>>> print(n1)
15
>>> print(n2)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    print(n2)
NameError: name 'n2' is not defined. Did you mean: 'n1'?
