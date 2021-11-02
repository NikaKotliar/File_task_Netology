from pprint import *

with open('recipes.txt', encoding='utf-8') as file:
    cook_book = {}
    for recipt in file:
        recipt_name = recipt.strip()
        counter = int(file.readline().strip())
        products = []
        for item in range(counter):
            ingridient, quantity, measuring = file.readline().split('|')
            products.append(
                {'ingridient': ingridient.strip(), 'quantity': quantity.strip(), 'measuring': measuring.strip()}
            )
        cook_book[recipt_name] = products
        file.readline()
    # pprint(cook_book)


# функция которая принимает на вход блюдо и количество порций и считает количество ингридиентов


def get_shop_list_by_dishes(dishes, person_count):
    shop_list_by_dishes = {}
    for dish in dishes:
        item = cook_book[dish]
        for ingridient in item:
            count = int(ingridient['quantity']) * person_count
            ingridient_name = ingridient['ingridient']
            if ingridient_name in shop_list_by_dishes.keys():
                measuring = shop_list_by_dishes[ingridient_name]
                measuring['quantity'] += count
            else:
                basic_measuring = {
                    'measuring': ingridient['measuring'],
                    'quantity': count
                }
                shop_list_by_dishes[ingridient_name] = basic_measuring
    pprint(shop_list_by_dishes)


get_shop_list_by_dishes(['Омлет', 'Омлет'], 2)
