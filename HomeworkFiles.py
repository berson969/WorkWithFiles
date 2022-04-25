# Домашнее задание к лекции «Открытие и чтение файла, запись в файл»

import os

FILE_PATH_RESULTS = os.path.join(os.getcwd(), 'results.txt')
FILE_PATH_RECIPES = os.path.join(os.getcwd(), 'recipes.txt')

print(FILE_PATH_RESULTS)

with open(FILE_PATH_RESULTS, 'w') as rs:
    rs.write('')


def print_cook_book(dict_cook):
    with open(FILE_PATH_RESULTS, 'a') as result:
        result.write('cook_book = {\n')
        print('cook_book = {')
        for key, value in dict_cook.items():
            result.write(f"'{key}': [\n")
            print(f"'{key}': [\n")
            for ingredient_full in value:
                result.write(f'\t {ingredient_full},\n')
                print(f'\t {ingredient_full},')
            result.write('\t]\n')
            print('\t]')
        result.write('}\n')
        print('}')


def print_shop_list(shop_list):
    with open(FILE_PATH_RESULTS, 'a') as result:
        result.write('\n\n{\n')
        print('\n\n{')
        for ing in shop_list:
            # for key,value in line.items():
            result.write(f"\t'{ing}':{shop_list[ing]},\n")
            print(f"\t'{ing}':{shop_list[ing]},")
        result.write('}\n')
        print('}')


def get_shop_list_by_dishes(dishes, person_count):
    get_shop_dict = {}
    for dish in dishes:
        for quantity_dict in cook_book[dish]:
            ingredient = quantity_dict['ingredient_name']
            if ingredient in get_shop_dict.keys():
                quantity = int(quantity_dict['quantity']) * person_count + int(get_shop_dict[ingredient]['quantity'])
            else:
                quantity = int(quantity_dict['quantity']) * person_count
            get_shop_dict[ingredient] = {'measure': quantity_dict['measure'], 'quantity': quantity}
    return get_shop_dict


with open(FILE_PATH_RECIPES) as r:
    recipes = []
    for line in r:
        recipes.append(line.strip())

    cook_book = {}
    i = 0
    while i < len(recipes):
        name_dish = recipes[i]
        count_ingredient = int(recipes[i + 1])
        dish_list = []
        for j in range(count_ingredient):
            dish_element = recipes[i + j + 2].split('|')
            ingredient = dict(ingredient_name=dish_element[0], quantity=int(dish_element[1]),
                              measure=dish_element[2].rstrip('\n'))
            dish_list.append(ingredient)
            cook_book[name_dish] = dish_list
        i += j + 4

print_cook_book(cook_book)
list_to_go_shop = get_shop_list_by_dishes(['Фахитос', 'Омлет'], 5)
print_shop_list(list_to_go_shop)
