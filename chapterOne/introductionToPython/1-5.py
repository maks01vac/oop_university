# 1 
# Напишите несколько строк кода, выводящих на экран ваше имя и почтовый адрес. 
# Адрес напишите в формате, принятом в вашей стране. 
# Никакого ввода от пользователя ваша первая программа принимать не будет, 
# только вывод на экран и больше ничего.

print("Maks")
print("Krasnodar")
print("Dimitrova street")
print("number 200")


# 2 Напишите программу, запрашивающую у пользователя его имя. В ответ 
# на ввод на экране должно появиться приветствие с обращением по имени, 
# введенному с клавиатуры ранее.

name = input("Введите имя: ")
print("Hello ",name)

# 3 Напишите программу, запрашивающую у  пользователя длину и  ширину 
# комнаты. После ввода значений должен быть произведен расчет площади 
# комнаты и выведен на экран. Длина и ширина комнаты должны вводиться 
# в формате числа с плавающей запятой. Дополните ввод и вывод единицами 
# измерения, принятыми в вашей стране. Это могут быть футы или метры

widthRoom = float(input("Введите ширину комнаты: "))
lengthRoom = float(input("Введите длину комнаты: "))

roomArea = widthRoom*lengthRoom

print("Площадь комнаты:", roomArea)

#4 Создайте программу, запрашивающую у  пользователя длину и  ширину 
# садового участка в футах. Выведите на экран площадь участка в акрах.


widthLand = float(input("Введите ширину садового участках в футах: "))
lengthLand = float(input("Введите длину садового участках в футах: "))

landArea = (widthLand*lengthLand)/43560

print("Площадь садового участка в акрах:", landArea)

#5 Во многих странах в стоимость стеклотары закладывается определенный 
# депозит, чтобы стимулировать покупателей напитков сдавать пустые бутылки. 
# Допустим, бутылки объемом 1 литр и меньше стоят $0,10, а бутылки большего объема – $0,25.
# Напишите программу, запрашивающую у пользователя количество бутылок каждого размера. 
# На экране должна отобразиться сумма, которую 
# можно выручить, если сдать всю имеющуюся посуду. Отформатируйте 
# вывод так, чтобы сумма включала два знака после запятой и дополнялась 
# слева символом доллара.

smallBottle = int(input("Введите количество бутылок объемом 1 литра и меньше: "))
bigBottle = int(input("Введите количество бутылок объемом больше 1 литра: "))

ernings = smallBottle*0.1 + bigBottle*0.25

float('{:.2f}'.format(ernings))

print('Выручка с продажи бутылок составляет $',ernings)