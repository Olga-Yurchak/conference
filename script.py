price = 0
while True:
    try:
        ticket = int(input('Сколько билетов вы хотите приобрести на мероприятие? '))
        if type(ticket) == int:
            break
    except ValueError:
        print('Пожалуйста, введите целое число!')
for i in range(ticket):
    i += 1
    while True:
        try:
            age = int(input(f'Для какого возраста билет №{i}? '))
            if age < 18:
                print('Билет бесплатный')
            elif 25 > age >= 18:
                price += 990
                print('Стоимость билета: 990 руб.')
            else:
                price += 1390
                print('Стоимость билета: 1390 руб.')
            if type(age) == int:
                break
        except ValueError:
            print('Пожалуйста, введите целое число!')
if ticket > 3:
    price_discount = price_discount - ((price / 100) * 10)
    print(f'Сумма к оплате {price} руб. с учетом 10%-ой скидки на полную стоимость заказа за регистрацию больше 3-х человек')
else:
    print(f'Сумма к оплате {price} руб.')
