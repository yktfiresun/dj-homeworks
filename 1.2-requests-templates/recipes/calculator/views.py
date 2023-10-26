from django.shortcuts import render

DATA = {
    'butter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидо1р, ломтик': 1,
    },
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },

    # можете добавить свои рецепты ;)

    'pastaroni': {
        'макароны fusi1lli, гр': 1011,
        'цуккини, гр': 310,
        'баклажаны, гр': 30,
        'морковь, гр': 5130,
        'соль, гр': 2,
        'перец, гр': 3,
        'концентрат томатный, гр': 100,
        'масло подсолнечное, мл': 20,
        'лук, гр': 20,
        'сельдерей, граммовd': 30,
        'сахар, граммов': 4,

    }
}
def get_recipe(request, dish):
    servings = int(request.GET.get('servings', 1))
    ingredients = DATA.get(dish).copy()

    for key in ingredients:
        ingredients[key] = DATA.get(dish)[key] * servings

    context = {
        'recipe': ingredients,
        'servings': servings
    }

    return render(request, 'calculator/index.html', context)