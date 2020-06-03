import random
# Щепотка цифр
str1 = '0123456789'
print(str1)
# Щепотка строчных букв
str2 = 'qwertyuiopasdfghjklzxcvbnm'
print(str2)
# Щепотка прописных букв. Готовится преобразованием str2 в верхний регистр.
str3 = str2.upper()
print(str3)
# Выведет: 'QWERTYUIOPASDFGHJKLZXCVBNM'

# Соединяем все строки в одну
str4 = str1+str2+str3
print(str4)
# Выведет: '123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'

# Преобразуем получившуюся строку в список
ls = list(str4)
# Тщательно перемешиваем список
random.shuffle(ls)
# Извлекаем из списка 12 произвольных значений
psw = ''.join([random.choice(ls) for x in range(12)])
# Пароль готов
print(psw)
