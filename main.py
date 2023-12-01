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
    ingr_dict = {}
    for i in dishes:
        for ingredient in my_cook_book()[i]:
            name = ingredient['ingredient_name']
            if name in ingr_dict:
                ingr_dict[name] = {'measure': ingredient['measure'],
                                   'quantity': int(ingredient['quantity'] + (
                                           ingr_dict[name]['quantity'] / person_count)) * person_count}
            else:
                ingr_dict[name] = {'measure': ingredient['measure'],
                                   'quantity': ingredient['quantity'] * person_count}

    return ingr_dict


pprint(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2))
