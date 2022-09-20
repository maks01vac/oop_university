from math import pi
from math import sqrt

#16

r = int(input('Введите радиус: '))

square = pi*(r*r)
volume = 4*(pi*r**3)/3

print('Площадь круга -',square)
print('Объем шара -',volume)

#17

m = float(input('Введите массу воды: '))
T= float(input('Введите разницу температуры: '))

C = 4.186

q = m*C*T

kVt = q/3600000
price = kVt*8.9

print('Столько нужно энергии:',q)
print('Столько нужно центов10:',price)

#18

r = float(input('Введите радиус цилиндра: '))
height= float(input('Введите высоту цилиндра '))

volume = pi*r*r*height

print('Объем цилиндра:',volume)

#19

d = float(input('Введите высоту от земли: '))
vi = 0
a = 9.8
3
vf = sqrt(vi*vi + 2*a*d)

print('Скорость при соприкосновении с землей:',vf)

#20

