#  Created by Artem Manchenkov
#  artyom@manchenkoff.me
#
#  Copyright © 2019
#
#  Примеры базового синтаксиса и работа с типами данных
#  Числа, строки, списки, булево значение
#
# коментарий Ctrl + /
simple = 10
result = simple + 10

print(1 / 2)
print(1 // 2)
print(1 % 2)

print(type(simple))

s1 = int(0.8)
s2 = 10.0
print(type(s1))
print(type(s2))
name = "fJoan"
print(name)
print(name + ' ' + name)
print(name * 3)
print("-"*30)
name = name.capitalize()
print(name)
name = name.upper()
print(name)


age = int(input("Введите ваш возраст: "))
print(age)
if age > 10:
    print("прівет")
else:
    print("Пока")
