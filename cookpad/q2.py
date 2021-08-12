from typing import List, Any
import requests
import sys
import copy


class Category:
    def __init__(self, name: str, recipes: int, subcategories: List[Any]) -> None:
        self.name = name
        self.subcategories = subcategories
        self.recipes = recipes

def count_total_recipe_num(category: Category) -> int:
    if len(category.subcategories) > 0:
        total_recipe_num = 0
        for subcategory in category.subcategories:
            total_recipe_num += count_total_recipe_num(subcategory)
        return total_recipe_num
    else:
        return category.recipes


def get_root_category(name: str, category: Category) -> Category:
    if category.name == name:
        return category
    elif len(category.subcategories) > 0:
        for subcategory in category.subcategories:
            if get_root_category(name, subcategory) != None and subcategory.name == name:
                print(name)
                return copy.deepcopy(subcategory)
        return None
    else:
        return None


def parse_category_tree(data) -> Category:
    name = data["name"]
    subcategories, recipes = [], 0
    if data.get("subcategories") != None:
        for subcategory_data in data["subcategories"]:
            subcategory = parse_category_tree(subcategory_data)
            subcategories.append(subcategory)
        return Category(name=name, recipes=0, subcategories=subcategories)
    else:
        recipes = data["recipes"]
        return Category(name=name, recipes=recipes, subcategories=[])


if __name__ == "__main__":
    url = "https://static.cookpad.com/hr/screen/categories.json"
    res = requests.get(url)
    print(get_root_category(
        sys.argv[1], parse_category_tree(res.json())))
    print(count_total_recipe_num(get_root_category(
        sys.argv[1], parse_category_tree(res.json()))))
