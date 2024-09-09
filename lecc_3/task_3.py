#  Создайте вручную кортеж содержащий элементы разных типов. 
# ✔ Получите из него словарь списков, где:
# ключ — тип элемента,
# значение — список элементов данного типа

tup = (5, 8.5, 'qwe', 10, 'abc', -3.5)
clovar = {}

for i in tup:
    key = type(i)
    if key not in clovar:
        clovar[key] = []
    clovar[key].append(i)
print(clovar)








