print ("цена билета: Дети до 18 лет бесплатно; от 18 до 25 лет - цена 990 руб.; старше 25 лет - полная стоимость 1390 руб.")
print ("При покупке от 3х билетов, действует скидка 10%")

b = int(input ("укажите количество билетов - "))
a = int(input ("укажите свой возраст - "))
x, y, z = 0, 990, 1390
if a < 18:
    price = x
    print ("Для Вас проход бесплатный! К оплате - ", x)
elif 18 <= a < 25:
    price = y
    print("Цена 1 билета - ", y)
else:
    price = z
    print("Цена 1 билета - ", z)

c = b * price
if b >= 2:
    print ("к оплате - ", c)
else:
    c = (b * price) * 0.9
