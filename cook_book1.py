#1 Задача

with open('recepies.txt', encoding='utf-8') as file:
    cook_book = {}
    for i in file:
        recepie_name = i.strip()
        ingredients_count = file.readline()
        ingredients = []
        for p in range(int(ingredients_count)):
            recepie = file.readline().strip().split(' | ')
            ingredient_name, quantity, measure = recepie
            ingredients.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
        file.readline()
        cook_book[recepie_name] = ingredients
print(cook_book)

#2 Задача

def get_shop_list_by_dishes(person_count: int, dishes: list):
    result = {}
    for dish in dishes:
        if dish in cook_book:
            for consist in cook_book[dish]:
                if consist['ingredient_name'] in result:
                    result[consist['ingredient_name']]['quantity'] += int(consist['quantity'])  * person_count
                else:
                    result[consist['ingredient_name']] = {'measure': consist['measure'],'quantity': int(consist['quantity']) * person_count}
        else:
            print('Такого блюда нет в книге')
            
    return result
    
print(get_shop_list_by_dishes(2, ['Запеченный картофель', 'Омлет']))






















