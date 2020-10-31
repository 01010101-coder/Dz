# 3. Проверьте, содержит ли слово определенные буквы. Буква вводится пользователем
import re

word = input('Enter a word: ')

letter = input('Enter letter: ')

result = re.findall(letter, word)

if len(result) > 0:
    print('В слове есть буквы', letter)
else:
    print('В слове нету буквы', letter)
