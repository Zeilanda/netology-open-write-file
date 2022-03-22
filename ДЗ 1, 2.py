from typing import List


def make_cook_book(file_name: str, mode: str, encoding: str) -> dict[str: List[dict]]:
    with open(file_name, mode, encoding=encoding) as file:
        result = [line.strip() for line in file.readlines()]
        cook_list = []
        inter_list = []
        for data in result:
            if not data == '':
                inter_list.append(data)
            else:
                cook_list.append(inter_list)
                inter_list = []
        cook_list.append(inter_list)
        cook_dict = {}
        for info in cook_list:
            cook_dict[info[0]] = list(info[2:])
        for key, value in cook_dict.items():
            composition = {}
            result = []
            for name in value:
                product, quantity, measure = name.split(' | ')
                composition['ingredient_name'] = product
                composition['quantity'] = int(quantity)
                composition['measure'] = measure
                result.append(composition)
                composition = {}
            cook_dict[key] = result
    return cook_dict


def get_shop_list_by_dishes(dishes: List[str], person_count: int) -> dict[str: dict]:
    ingredients = {}
    composition = {}
    for dish in dishes:
        if dish in cook_book:
            for dict_ingredient in cook_book[dish]:
                composition['measure'] = dict_ingredient['measure']
                if dict_ingredient['ingredient_name'] not in ingredients:
                    composition['quantity'] = dict_ingredient['quantity'] * person_count
                    ingredients[dict_ingredient['ingredient_name']] = composition
                else:
                    inter = ingredients[dict_ingredient['ingredient_name']]
                    inter['quantity'] += dict_ingredient['quantity'] * person_count

                composition = {}
    return ingredients


cook_book = make_cook_book('recipes.txt', 'r', 'utf-8')
print(get_shop_list_by_dishes(['Яичница с беконом', 'Омлет'], 3))
