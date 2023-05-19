import re
library = []
with open('synonyms.txt', 'r+') as file:
    for line in file:
        if line != "\n":
            library.append([i.lower().strip().replace(';', '') for i in line.split() if i != '-'])
    wordbook = {}
    for a in library:
        for b in a:
            wordbook[b] = {c for c in a if c!=b}
library = input('Введите слово: ').lower().strip()
if wordbook.get(library) == None:
    print("Данное слово не найдено")
else:
    q = (str(wordbook.get(library))).replace("'","").replace(',',';')[1:-1]
    if q[-1] == ';':
        q = q[0:-1]
    print(q)
    answer = input("Синоним(ы) устраивают вас? y/n ").lower().strip()
    if answer == "n":
        word = input("Введите новый синоним: ")
        pattern = re.compile(q)
        with open('synonyms.txt', 'r+') as file:
            lines = file.readlines()
            file.seek(0)
            for line in lines:
                result = pattern.search(line)
                if result is None:
                    file.write(line)
                file.truncate()
        with open('synonyms.txt', 'a') as file:
            file.write(f"{library.capitalize()} - {word.lower().strip()}; {q}\n")
            print("Синоним добавлен в словарь")