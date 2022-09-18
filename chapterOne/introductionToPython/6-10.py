from math import log10

# 6

orderPrice = float(input("Введите сумму заказа в ресторане:"))

tax = orderPrice*0.13
tips = (orderPrice - tax)*0.18

total = tax + tips

print('Налог:', tax)
print('Чаевые:', tips)
print('Итог:',total)

#7

number = int(input('Введите число:'))

sum = (number*(number + 1))/2

print('Сумма натуральных положительных чисел от 1 до ',number," равнa:",int(sum))

#8

souvenir = int(input('Введите количество сувениров:'))
trinket = int(input('Введите количество безделушек:'))

totalWeight = (souvenir*75 + trinket*112)/1000

print('Общий вес посылки составляет ',totalWeight," кг")

#9

depositAmount = float(input('Введите сумму первоначального депозита -'))
numberOfYears = int(input('Введите количество лет депозита - '))

beginYear = 1
result =[]

while beginYear <= numberOfYears:

    depositAmount = depositAmount*1.04
    result.append(depositAmount)

    beginYear+=1

for i in range(len(result)):
    roundingArrayElement = round(result[i],2)
    print("Сумма депозита после",i+1,"года:",roundingArrayElement)

#10

a = int(input('Введите a: '))
b = int(input('Введите b: '))

print('cумма a и b:',a + b)
print('разница между a и b:',abs(a-b))
print('произведение a и b:',a*b)
print('частное от деления a на b:',a/b)
print('остаток от деления a на b:',a % b)
print('десятичный логарифм числа a:',log10(a))
print('результат возведения числа a в степень b:',a**b)

