# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого длинного 
# слова был один пробел между ним и номером строки.

clovo = 'В лесу родилась елочка'
count = 1
list_1 = clovo.split()
for i in list_1:
    print(count, i)
    count+=1