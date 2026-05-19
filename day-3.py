Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = 10
b = 10
print(a is b)
True
b = 257
a = 257
print(a is b)
False
>>> a = 256
>>> b = 256
>>> print(a is b)
True
>>> a = 10
>>> b = 10
>>> print(id(a), id(b))
140736103543880 140736103543880
>>> print(a is b)
True
>>> a = 10
>>> b = 10
>>> print(id(a), id(b))
140736103543880 140736103543880
>>> a = 10
>>> b = 20
>>> print(id(a), id(b))
140736103543880 140736103544200
>>> print(1 in [1,2,3,4,5])
True
>>> 
>>> a = [1,2,3]
>>> b = [1,2,3]
>>> print(a is b)
False
>>> print(a == b)
True
>>> a = 10
>>> b = 5
>>> print(a & b)
0
