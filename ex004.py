
# показать числа у которых последняя цифра без остатка делится на 4
count = int(input("n="))
index = 0
while index <= count:
    if (index % 10) % 4 == 0:
        print(index, end= " ")
    index += 1


    123 % 10 = 3
    55 % 10 = 5