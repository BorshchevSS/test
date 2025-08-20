sumPocupki = float(input("Введи сумму покупки: "))
age  = int(input("Введи возраст: "))

sumPay_1 = 100
skidca_sumPay_1 = 10 #Величина скидки в %
discount = 0

if sumPocupki >= sumPay_1:
    discount += skidca_sumPay_1

if age > 65:
    discount += 5

final_price = sumPocupki*(1-discount/100)

# if discount == 0
print(f"Общая скидка:{discount} \n Сумма покупки: {final_price:.2f}")