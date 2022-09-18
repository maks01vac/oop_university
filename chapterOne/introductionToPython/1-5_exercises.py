# 1

# print("Maks")
# print("Krasnodar")
# print("Dimitrova street")
# print("number 200")


# 2

# name = input("Введите имя: ")
# print("Hello ",name)

# 3

# widthRoom = float(input("Введите ширину комнаты: "))
# lengthRoom = float(input("Введите длину комнаты: "))

# roomArea = widthRoom*lengthRoom

# print("Площадь комнаты:", roomArea)

#4

# widthLand = float(input("Введите ширину садового участках в футах: "))
# lengthLand = float(input("Введите длину садового участках в футах: "))

# landArea = (widthLand*lengthLand)/43560

# print("Площадь садового участка в акрах:", landArea)

#5 

smallBottle = int(input("Введите количество бутылок объемом 1 литра и меньше: "))
bigBottle = int(input("Введите количество бутылок объемом больше 1 литра: "))

ernings = smallBottle*0.1 + bigBottle*0.25

float('{:.2f}'.format(ernings))

print('Выручка с продажи бутылок составляет $',ernings)