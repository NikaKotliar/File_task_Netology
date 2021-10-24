from pprint import *

with open('recipes.txt', encoding='utf-8') as file:
    result = {}
    for recipt in file:
        recipt_name = recipt.strip()
        counter = int(file.readline().strip())
        products = []
        for item in range(counter):
            ingridient, quantity, measuring = file.readline().split('|')
            products.append(
                {'ingridient': ingridient.strip(), 'quantity': quantity.strip(), 'measuring': measuring.strip()}
            )
        result[recipt] = products
        file.readline()
    pprint(result)
