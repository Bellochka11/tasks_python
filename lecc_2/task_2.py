# ✔ Напишите программу, которая получает целое число и возвращает 
# его двоичное, восьмеричное строковое представление.
# ✔ Функции bin и oct используйте для проверки своего 
# результата, а не для решения.
# Дополнительно:
# ✔ Попробуйте избежать дублирования кода 
# в преобразованиях к разным системам счисления
# ✔ Избегайте магических чисел
# ✔ Добавьте аннотацию типов где это возможно

# num = int(input())
# print(bin(num))
# print(oct(num))
# print(hex(num))


number = 16
print(bin(number), oct(number), hex(number))
result = ""
divider = int(input('Введите основание: '))
while number > 0:
    result = str(number % divider) + result
    number //= divider
print(result)