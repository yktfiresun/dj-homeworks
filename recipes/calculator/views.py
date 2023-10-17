from django.shortcuts import render

DATA = {
    'butter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
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
        'макароны fusilli, гр': 100,
        'цуккини, гр': 30,
        'баклажаны, гр': 30,
        'морковь, гр': 50,
        'соль, гр': 2,
        'перец, гр': 3,
        'концентрат томатный, гр': 100,
        'масло подсолнечное, мл': 20,
        'лук, гр': 20,
        'сельдерей, гр': 30,
        'сахар, гр': 4,

    }
}


# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

#def home1(request):
#    data = ["Первый элемент", "Второй элемент", "Третий элемент"]
#
#    context = {
#        'data': data
#    }
#    return render(request, 'calculator/home.html', context)

def butter(request):
    servings = int(request.GET.get('servings', 1))
    context ={
        'recipe': {
            'хлеб, ломтик': 1 * servings,
            'колбаса, ломтик': 1 * servings,
            'сыр, ломтик': 1 * servings,
            'помидор, ломтик': 1 * servings,
        }
    }

    return render(request, 'calculator/index.html', context)

def omlet(request):
    servings = int(request.GET.get('servings', 1))
    context = {
        'recipe': {
            'яйца, шт': 2 * servings,
            'молоко, л': 0.1 * servings,
            'соль, ч.л.': 0.5 * servings,
        }
    }

    return render(request, 'calculator/index.html', context)

def pasta(request):
    servings = int(request.GET.get('servings', 1))
    context = {
        'recipe': {
            'макароны, г': 0.3 * servings,
            'сыр, г': 0.05 * servings,
        }
    }

    return render(request, 'calculator/index.html', context)

def pastaroni(request):
    servings = int(request.GET.get('servings', 1))
    context = {
        'recipe': {
            'макароны fusilli, гр': 100 * servings,
            'цуккини, гр': 30 * servings,
            'баклажаны, гр': 30 * servings,
            'морковь, гр': 50 * servings,
            'соль, гр': 2 * servings,
            'перец, гр': 3 * servings,
            'концентрат томатный, гр': 100 * servings,
            'масло подсолнечное, мл': 20 * servings,
            'лук, гр': 20 * servings,
            'сельдерей, гр': 30 * servings,
            'сахар, гр': 5 * servings,
        }
    }

    return render(request, 'calculator/index.html', context)
