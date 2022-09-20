from math import sqrt
from math import tan
from math import pi

#21

b = float(input('Введите длину основания треугольника:'))
h = float(input('Введите высоту треугольника:'))

area = b*h/2

print('Площадь треугольника с основанием ',b,' и высотой ',h,' равна: ',area)

#22

s1 = float(input('Введите первую сторону треугольника:'))
s2 = float(input('Введите вторую сторону треугольника:'))
s3 = float(input('Введите третью сторону треугольника:'))

s = (s1 + s2 + s3)/2

area = sqrt(s*(s - s1)*(s - s2)*(s - s3))

print('Площадь треугольника с сторонами ',s1,', ',s2,', ',s3,' равна: ',area)

#23

s = float(input('Введите длину стороны многоугольника:'))
n = float(input('Введите количество сторон многоугольника:'))

area = (n*s*s)/(4*tan(pi/n))

print('Площадь многоугольника:',area)

#24

days = int(input('Введите количество дней:'))
hours = int(input('Введите количество часов:'))
minutes = int(input('Введите количество минут:'))
seconds = int(input('Введите количество секунд:'))

allSeconds = days*24*60*60 + hours*60*60 + minutes*60 + seconds

print('Общее количество секунд:',allSeconds)

#25

allSeconds = int(input('Введите общее количество секунд:'))


days = allSeconds // (24*60*60)
allSeconds = allSeconds % (24*60*60)

hours = allSeconds // (60*60)
allSeconds = allSeconds % (60*60)

minutes = allSeconds // (60)
seconds = allSeconds = allSeconds % (60)

print(days,':',hours,':',minutes,':',seconds)