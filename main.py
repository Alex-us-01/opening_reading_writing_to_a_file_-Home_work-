from pprint import pprint


def my_cook_book():
    with open('recipes.txt', encoding='utf-8') as f:
        cook_book = {}
        for txt in f.read().split('\n\n'):
            name, number, *args = txt.split('\n')
            tmp = []
            for arg in args:
                ingredient_name, quantity, measure = map(lambda x: int(x) if x.isdigit() else x, arg.split(' | '))
                tmp.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
            cook_book[name] = tmp
        return cook_book


pprint(my_cook_book())


def get_shop_list_by_dishes(dishes, person_count):
    ing_dict = {}
    for i in dishes:
        for ingredient in my_cook_book()[i]:
            name = ingredient['ingredient_name']
            if name in ing_dict:
                ing_dict[name] = {'measure': ingredient['measure'],
                                  'quantity': int(ingredient['quantity'] + (
                                          ing_dict[name]['quantity'] / person_count)) * person_count}
            else:
                ing_dict[name] = {'measure': ingredient['measure'],
                                  'quantity': ingredient['quantity'] * person_count}

    return ing_dict


pprint(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2))


def read_file(file):
    with open(file, encoding='utf-8') as f:
        text = f.readlines()
    return text


list_files = ['1.txt', '2.txt', '3.txt']


def read_files(files):
    list_text = []
    for element in files:
        with open(element, encoding='utf-8') as f:
            text = f.readlines()
            list_text.append([len(text), element, text])
    list_text.sort()
    return list_text




def create_new_file(list_text: list, new_file):
    with open(new_file, 'w', encoding='utf-8') as f:
        for element in list_text:
            f.write(element[1] + '\n')
            f.write(str(element[0]) + '\n')
            for el in element[2]:
                if '\n' in el:
                    f.write(el.lstrip())
                else:
                    f.write(el.lstrip() + '\n')


create_new_file(read_files(list_files), 'main.txt')
