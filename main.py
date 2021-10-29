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
shop_list_by_dishes = {}

def get_shop_list_by_dishes(dishes, person_count):
    for dish in dishes:
        for recipt, item in cook_book.items():
            if dish == recipt:
                for ingridient in item:
                    count = int(ingridient['quantity']) * person_count
                    measuring = {'measuring': ingridient['measuring'], 'quantity': count}
                    shop_list_by_dishes = {ingridient['ingridient']: measuring}
                    print(shop_list_by_dishes)

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
