# -*- coding: utf-8 -*-
"""lab3

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zI5Ve12qrAU-VRQ19sOWdpyJpHtMDZ2E
"""

a = int(input())
if a == 1:
  print('Январь')
elif a == 2:
  print('Февраль')
elif a == 3:
  print('Март')
elif a == 4:
  print('Апрель')
elif a == 5:
  print('Май')
elif a == 6:
  print('Июнь')
elif a == 7:
  print('Июль')
elif a == 8:
  print('Август')
elif a == 9:
  print('Сентябрь')
elif a == 10:
  print('Октябрь')
elif a == 11:
  print('Ноябрь')
elif a == 12:
  print('Декабрь')

a = int(input())
if a % 2 == 1:
  print("нечетное")
elif a%2 !=1:
  print("четное")

N = int(input())
if N > 40:
  print("stonks c:")
elif N < 40:
  print("not stonks :c")

def is_year_leap():
  year = int(input("Введите год"))
  if year % 4 == 0 or (year % 100 != 0 and year % 400 == 0):
    return True
  else:
    return False
is_year_leap()

def is_prime():
  n = int(input())
  for i in range(2, n):
    if n % i == 0:
      return False
    else:
      return True
is_prime()

a=float(input())
b=float(input())
if (a/b>=3.6) or (b>=((-138/2)**1.3) and b>=(abs((-69/28**5.1)*4))):
  a,b = b,a
print(a,b)

a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
k=0
s=0
g=0
if a!=b!=c!=d!=e:
  print(True)
if a%2==0:
  k += 1
if b%2==0:
  k += 1
if c%2==0:
  k += 1
if d%2==0:
  k += 1
if e%2==0:
  k += 1
print(k)
if a<0:
  s += 1
if b<0:
  s += 1
if c<0:
  s += 1
if d<0:
  s += 1
if e<0:
  s += 1
print(s)
if a in range(-256 , 1024):
  g += 1
if b in range(-256 , 1024):
  g += 1
if c in range(-256 , 1024):
  g += 1
if d in range(-256 , 1024):
  g += 1
if e in range(-256 , 1024):
  g += 1
print(g)