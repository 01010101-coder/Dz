# 2. Среди текста найти автомобильные номера.
# Номера могут быть вида: XXXX YY-X или YY-X XXXX (это грузовые).
import re

text = '5647 OJ-5 OK-5 4543 65-2 4324 KIOP 44-F 4390 FF-3 GFHD4345 GG-4S ro24jfp3hrf7777 MM-7jfhd'

result1 = re.findall(r'(\b\d{4}\ \w[A-Z]+\-\d)\b' ,text)
result2 = re.findall(r'(\b\w[A-Z]+\-\d\ \d{4})\b', text)

result = result1 + result2

print(result)