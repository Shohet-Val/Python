
#прочитать сайт и посчитать статистику использования слов с# или python
from urllib.request import urlopen

html = urlopen("https://ru.wikipedia.org/wiki/Python").read().decode('utf-8')
s = str(html)
print('Сравнительная частота в статьи из Википедии о Питоне')
print('Частота С++ ', s.count('C++'))
print('Частота Python ', s.count('Python'))
#
"""
m_htm = urlopen("https://ru.wikipedia.org/wiki/C++").read().decode('utf-8')
r = str(html)
print('Сравнительная частота в статьи из Википедии о Pascal')
print('Частота Java ', r.count('Java'))
print('Частота C# ', r.count('C#'))
print('Частота JavaScript ', r.count('JavaScript'))
"""
#https://stepik.org/media/attachments/lesson/209717/1.html
print('+++++ Задание +++++')
m_html = urlopen("https://stepik.org/media/attachments/lesson/209717/1.html").read().decode('utf-8')
j = str(m_html)
text_site = str(m_html)
#print(text_site)
print('Сравнительная частота в статьи из Википедии о Питоне')
print('Частота Python ', j.count('Python'))
print('Частота C++ ', j.count('C++'))
