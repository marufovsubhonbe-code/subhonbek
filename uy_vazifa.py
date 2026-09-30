# SLAYD 4 

# 1
print(3 ** 80)
print(len(str(3 ** 80)))

# 2
son = 3_480_750
print(son)
print(len(str(son)))

# 3
natija = True + True + True + False
print(natija)
print(type(False))


# SLAYD 5 

# 1
print(0.1 + 0.7)
print(0.1 + 0.7 == 0.8)

# 2
import math

print(math.isclose(0.1 + 0.7, 0.8))

# 3
narx = 4.35
print(narx * 3)


# AMALIYOT 6

# 1
print(2 ** 90)
print(2 ** 300)
print(len(str(2 ** 300)))

# 2
print(0.3 + 0.6 == 0.9)
print(math.isclose(0.3 + 0.6, 0.9))

# 3
print(2_500_000 == 2500000)

# 4
print(type(12))
print(type(12.0))
print(type(False))

# SLAYD 7 

# 1
print(17 / 4)
print(17 // 4)
print(17 % 4)
print(3 ** 5)

# 2
print(divmod(17, 4))

# 3
print(-17 // 4)

# 4
print(type(12 / 4))

# 5
print(divmod(380, 15))


# SLAYD 8

# 1
print(round(4.5))
print(round(5.5))
print(round(6.5))

# 2
print(round(2.71828, 3))

# 3
import math

print(math.floor(7.8))
print(math.ceil(7.2))

print(math.trunc(-7.8))
print(math.floor(-7.8))


# AMALIYOT 9

# 1
print(1000 // 60)
print(1000 % 60)

# 2
print(divmod(1000, 60))

# 3
print(round(3.5))
print(round(4.5))
print(round(7.5))
print(round(8.5))

# 4
print(math.floor(5.2))
print(math.ceil(5.2))
print(math.trunc(5.2))

print(math.floor(-5.2))
print(math.ceil(-5.2))
print(math.trunc(-5.2))

# Slayd 10

from decimal import Decimal
from fractions import Fraction

# 1
natija1 = Decimal('0.3') + Decimal('0.6')
print("1.", natija1, "->", natija1 == Decimal('0.9')) 

# 2
print("2. Decimal(0.3)   =", Decimal(0.3))    
print("   Decimal('0.3') =", Decimal('0.3'))  
print("   To'g'risi: Decimal('0.3') (float noaniq saqlanadi, satr esa aniq)")

# 3
print("3.", Fraction(1, 4) + Fraction(1, 12))

# 4
print("4a.", Fraction(2, 5) * 3)
print("4b.", Fraction(5, 6) - Fraction(1, 3))

# Slayd 11
print(bin(12), oct(80), hex(200)) 
print(int('1101', 2), int('c8', 16))

# Amaliyot 12
print(bin(100), oct(100), hex(100))  
print(int('10000000', 2))            

import math
from decimal import Decimal

#14
matn = 'Samarqand'
royxat = ['Olim', 'Zilola', 'Bobur', 'Laylo']
juftlik = (39.65, 66.96)
oraliq = range(7)
for i in (matn, royxat, juftlik, oraliq):
    print(len(i), i[0])
for i in (matn, royxat, juftlik, oraliq):
    print(i[-1])
try:
    t = {10, 20, 30}
    print(t[0])
except TypeError as e:
    print(e)

#15
royxat = ['Olim', 'Zilola']
royxat.append('Bobur')
print(royxat)
matn = 'Olim'
print(matn.replace('O', 'A'))
print(matn)
juftlik = (5, 8)
try:
    juftlik[1] = 10
except TypeError as e:
    print(e)

#16
royxat = ['Olim']
a = id(royxat)
royxat.append('Zilola')
print(a == id(royxat))
satr = 'samarqand'
print(satr.upper())
print(satr)
print(id(satr) == id(satr.upper()))
try:
    t = (7, 9)
    t[0] = 1
except TypeError as e:
    print(e)
print(tuple(['a', 'b', 'c']))
print(list((4, 5, 6)))

#17
shahar = 'Samarqand'
print(shahar[0], shahar[4], shahar[-1], shahar[-3])
print(shahar[50:])
try:
    print(shahar[50])
except IndexError as e:
    print(e)
talaba = ['Olim', 'Zilola', 'Bobur', 'Laylo']
print(talaba[len(talaba) - 1])
print(talaba[-1])

#18
s = 'Namangan'
print(s[0:4], s[:3], s[4:])
print(s[::2])
print(s[::-1])
sonlar = [15, 25, 35, 45, 55, 65]
print(sonlar[1:4])
print(sonlar[-3:])
print(sonlar[::3])

#19
soz = 'Mustaqillik'
print(soz[3:8])
print(soz[::-1])
sonlar = [10, 20, 30, 40, 50, 60, 70, 80]
print(sonlar[::3])
print(sonlar[1::2])
nusxa = sonlar[:]
nusxa.append(90)
print(sonlar)
print(nusxa)

#20
print(list(range(7)))
print(list(range(3, 9)))
print(list(range(1, 20, 4)))
print(list(range(10, 0, -2)))
r = range(0, 2000000, 5)
print(len(r))
print(r[100])
print(1999995 in r)
print(1999997 in r)
for i in range(4):
    print(i, 'Assalomu alaykum')

#21
a = [5, 7, 9]
print(a + [11, 13])
print(a * 3)
b = [3, 8, 3, 5, 3]
print(8 in b)
print(b.count(3))
print(b.index(5))
c = [12, 4, 19, 7]
print(len(c), min(c), max(c), sum(c))
print('qand' in 'Samarqand')
print('Qand' in 'Samarqand')

#22
koordinata = (39.65, 66.96)
kenglik, uzunlik = koordinata
print(kenglik, uzunlik)
mevalar = ['olma', 'nok', 'uzum', 'anor', 'shaftoli']
birinchi, *qolgan = mevalar
print(birinchi, qolgan)
x, y = 15, 40
x, y = y, x
print(x, y)

#23
toq = list(range(1, 41, 2))
print(toq)
print(sum(toq))
print('Samarqand qandolatchilari'.count('qand'))
ismlar = ['Bobur', 'Laylo', 'Olim', 'Zilola']
birinchi, *qolgan = ismlar
print(birinchi, qolgan)
narx1, narx2 = 12000, 8500
narx1, narx2 = narx2, narx1
print(narx1, narx2)

#24
print(0.2 + 0.4 == 0.6)
print(math.isclose(0.2 + 0.4, 0.6))
a = [7, 8]
b = a
b.append(9)
print(a)
c = a[:]
c.append(10)
print(a, c)
jadval = [[1] * 2] * 4
jadval[1][0] = 5
print(jadval)
jadval = [[1] * 2 for _ in range(4)]
jadval[1][0] = 5
print(jadval)

#25
narx = Decimal('24.75')
print(narx * 4)
shaharlar = ['Toshkent', 'Buxoro', 'Xiva']
print(shaharlar[-1])
aholi = 3_000_000
print(aholi == 3000000)
oylar = ('Yan', 'Fev', 'Mar')
try:
    oylar[0] = 'Yanvar'
except TypeError as e:
    print(e)

#26
print(len(str(3 ** 200)))
print(0.1 + 0.7)
print(math.isclose(0.1 + 0.7, 0.8))
print(-9 // 4)
print('Andijon'[::-1])
print((1, 2, 3)[::-1])
print([4, 5, 6][::-1])
a = [2, 4]
b = a
c = a[:]
print(b is a)
print(c is a)