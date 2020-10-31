# 5. Найти доменные имена для протоколов http и https с необязательным слешем в конце.
# Пример:
# https://example.com/ - да
# example.com - нет
# розы.бел - нет
import re

text = ['https://example.com/', 'example.com', 'розы.бел', 'http://ochenKrutoeImya.ru/', 'http://nblblb.ru']


itog = []

for i in range(len(text)):
    result1 = re.findall('http:', text[i])
    result2 = re.findall('https:', text[i])
    result = result1 + result2
    if text[i][0:5] in result or text[i][0:6] in result:
        itog.append(text[i])
    else:
        pass

print(itog)