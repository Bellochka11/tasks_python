# Вручную создайте список с целыми числами, которые 
# повторяются. Получите новый список, который содержит 
# уникальные (без повтора) элементы исходного списка. 
# ✔ *Подготовьте два решения, короткое и длинное, которое 
# не использует другие коллекции помимо списков.

list_1 = [3,4,3,7,9,5,7,9]
list_2 = list(set(list_1))
print(list_2)

#decision 2
list_3 = []
for i in list_1:
    if i not in list_3:
        list_3.append(i)
print(list_3)