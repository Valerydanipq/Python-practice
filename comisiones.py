name = input("Please tell me your name: ")
sales = input ("Say your total sales of the month : ")

sales = int(sales)

comission = sales * 13 / 100

comission = round(comission)


print(f"Hello {name}, your commissions of this month are of ${comission}")

name = input("Please tell me your name: ")
sales = int(input ("Say your total sales of the month : "))


comission = round(sales * 13 / 100,2)

print(f"Hello {name}, your commissions of this month are of ${comission}")
