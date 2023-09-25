# Вывести последнюю букву в слове
word = 'Архангельск'
print(f'>>> Последняя буквa в слове "{word}": {word[-1]}')


# Вывести количество букв "а" в слове
# если не учитывать заглавную...
word = 'Архангельск'
counter = 0
for char in word:
    if char == 'а':
        counter+=1
print(f'\n>>> Кол-во букв "а" в слове "{word}" (не учитывая заглавную): {counter}')

# Вывести количество гласных букв в слове
word = 'Архангельск'
cntr = 0
vowels = set("ауоыэяюёие")
for char in word.lower():
    if char in vowels:
        cntr +=1
print(f'\n>>> Гласных в слове "{word}": {cntr}')

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(f'\n>>> Кол-во слов в предложении "{sentence}": {len(sentence.split())}')


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
print(f'\n>>> Первые буквы каждого слова из предложения "{sentence}":')
for word in sentence.split():
    print(word[0])

# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
words_amount = len(sentence.split())
letters_amount = 0
for char in sentence:
    if char != ' ':
        letters_amount+=1
print(f'\n>>> Средняя длина слова в строке "{sentence}": {letters_amount/words_amount}')
