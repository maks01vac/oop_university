import math

# 11

MPG = float(input('Введите расход топлива в милях на галлон:'))

lpg = 3.785 #литров в галлоне
kmpm = 1.609 #киллометров в миле

LPK = (100*lpg)/(kmpm*MPG)

print("Расход топлива в литрах на 100 км: ",LPK)

# 12

t1 = float(input('Введите широту первой точки - t1:'))
t1 = math.radians(t1)
t2 = float(input('Введите широту второй точки - t2:'))
t2 = math.radians(t2)

g1 = float(input('Введите долготу первой точки - g1:'))
g1 = math.radians(g1)
g2 = float(input('Введите долготу второй точки - g2:'))
g2 = math.radians(g2)

distance = 6371.01*math.acos(math.sin(t1)*math.sin(t2)+math.cos(t1)*math.cos(t2)*math.cos(g1-g2))

print('Расстояние между двумя точками равно: ',distance)


# 13

change = int(input('Введите количество сдачи в центах:'))

toonie = change//200
change = change % 200

loonie = change//100
change = change % 100

quarter = change//25
change = change % 25

tenCent = change//10
change = change % 10

fiveCent = change//5
change = change % 5

print('Вы нужно ',toonie,' toonie, ',loonie,' loonie, ',quarter, " по 25 cent, ", tenCent," по 10 cent, ",fiveCent," по 5 cent и ", change,"по 1 cent")

#14

a,b=map(int,input("Введите рост в футах и дюймах через пробел: ").split())

growth = a*12*2.54 + b*2.54

print('Ваш рост в см: ',growth)

#15

distanse = float(input('Введите расстояние в футах:'))

print('Расстояние в дюймах:',distanse*12)
print('Расстояние в ярдах:',distanse/3)
print('Расстояние в милях:',distanse/5280)
