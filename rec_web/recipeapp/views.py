from random import randint

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Recipe, Categories, Connection
from .forms import AddRecipeForm


def index(request):
    """Вывод главной страницы"""
    max_id = int(Recipe.objects.latest('id').id)
    list_id = []
    count = 0
    while count < 5:
        item = randint(1, max_id)
        if item not in list_id:
            list_id.append(item)
            count += 1
    list_rec = [get_object_or_404(Recipe, pk=list_id[i]) for i in range(len(list_id))]
    context = {'title': "Рецептикус", 'list_rec': list_rec}
    return render(request, "recipeapp/index.html", context=context)


def base_rec(request, recipe_id):
    """Основная страница с рецептом"""
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    steps = recipe.steps_cook.split('/')
    ingredients = recipe.ingredients.split('/')
    category = Connection.objects.filter(recipe=recipe).first()
    print(f'категория {category}')
    print(f'категория_итем {category.categ_rec.all()}')
    list_cat = [(i.name_category, i.difficulty) for i in category.categ_rec.all()]
    print(list_cat)
    return render(request, "recipeapp/base_recipe.html",
                  context={'title': recipe.title, 'recipe': recipe, 'steps': steps, 'list_cat': list_cat,
                           'ingredients': ingredients})


def all_recipe(request):
    """Выводит все рецепты"""
    max_id = int(Recipe.objects.latest('id').id)
    list_rec = []
    for i in range(1, max_id + 1):
        list_rec.append(get_object_or_404(Recipe, pk=i))
    context = {'title': "Все рецепты", 'list_rec': list_rec}
    return render(request, "recipeapp/all_recipe.html", context=context)


def add_recipe(request):
    """Переход на страницу добавления рецепта и его добавление"""
    if request.method == 'POST':
        form = AddRecipeForm(request.POST, request.FILES)
        context = {'title': "Добавить рецепт", 'form': form}
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            ingredients = form.cleaned_data['ingredients']
            steps_cook = form.cleaned_data['steps_cook']
            time_cook = form.cleaned_data['time_cook']
            author = form.cleaned_data['author']
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
            recipe = Recipe(title=title, description=description, ingredients=ingredients, steps_cook=steps_cook,
                            time_cook=time_cook, author=author, image=image)
            recipe.save()
            connect = Connection(recipe=recipe)
            connect.save()
            a = form.cleaned_data['category']
            categ = Categories.objects.filter(name_category=a.split('/')[0], difficulty=a.split('/')[1]).first()
            connect.categ_rec.add(categ.id)
            connect.save()
    else:
        form = AddRecipeForm()
        context = {'title': "Добавить рецепт", 'form': form}
    return render(request, "recipeapp/add_recipe.html", context=context)


def about(request):
    return HttpResponse("About us")
