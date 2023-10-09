from choice_file import choice_number_file

def copy_row():
    x = choice_number_file()
    if x == 1:
        with open(f'db/data_{x}.txt', 'r', encoding='utf-8') as file_1:
            with open(f'db/data_{2}.txt', 'r', encoding='utf-8') as file_2:
                    data = file_1.readlines()
                    file_2.writelines(data)
    else:
        with open(f'db/data_{x}.txt', 'r', encoding='utf-8') as file_1:
            with open(f'db/data_{1}.txt', 'r', encoding='utf-8') as file_2:
                    data = file_1.readlines()
                    file_2.writelines(data)
    print('успешно скопировано!')
