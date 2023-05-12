import random
input_word = input('Введите слово: ')
file_path = 'synonyms.txt'
synonyms_dict = dict()
try:
    with open(file_path, 'r', encoding='UTF-8') as f:
        synonyms = f.read().split('\n')
    for line in synonyms:
        if line:
            word = line.split('-')[0].strip().lower()
            if word not in synonyms_dict:
                synonyms_dict[word] = [x.strip() for x in line.split('-')[1].strip().split(';')]
            else:
                synonyms_dict[word].extend([x.strip() for x in line.split('-')[1].strip().split(';') if x])

    if input_word.lower() in synonyms_dict:
        while True:
            return_synonym = random.choice(synonyms_dict[input_word.lower()])
            if return_synonym:
                print(return_synonym)
                break
        while True:
            synonym_correctness = input('Синоним устраивает?\n'
                                        '1. Да\n'
                                        '2. Нет\n')
            if synonym_correctness == '1':
                break
            elif synonym_correctness == '2':
                new_synonym = input('Введите новый синоним: ')
                if new_synonym not in synonyms_dict[input_word.lower()]:
                    synonyms_dict[input_word.lower()].append(new_synonym)
                    string_to_write = ''
                    for key in synonyms_dict:
                        synonyms_dict[key] = list(filter(None, synonyms_dict[key]))
                    for word, synonym in synonyms_dict.items():
                        string_to_write += f'{word} - {"; ".join(synonym)}\n'
                    with open(file_path, 'w', encoding='UTF-8') as f:
                        f.write(string_to_write)
                else:
                    print('\033[31mСлово уже имеется в словаре.\033[0m')
                break
    else:
        print('\033[31mСлово отсутствует в файле.\033[0m')
except FileNotFoundError:
    print(f'\033[31mФайл {file_path} не найден.\033[0m')