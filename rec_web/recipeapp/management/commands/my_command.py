from django.core.management.base import BaseCommand
from recipeapp.models import Recipe
from recipeapp.models import Categories
from recipeapp.models import Connection


class Command(BaseCommand):
    help = "Create recipe, description <= 296"

    def handle(self, *args, **kwargs):
        # description = 'Яблочный_пирог Яблочный_пирог Яблочный_пирог Яблочный_пирог Яблочный_пирог Яблочный_пирог' \
        #              'Яблочный_пирог Яблочный_пирог Яблочный_пирог Яблочный_пирог Яблочный_пирог Яблочный_пирог' \
        #              'Яблочный_пирог Яблочный_пирог Яблочный_пирог Яблочный_пирог Яблочный_пирог Яблочный_пирог' \
        #              'Яблочный_пирог Яблочный_пирог'
        # recipe = Recipe(title='Апельсиновый пирог', description=description, ingredients='Мука/Соль/Яйца/Яблоки',
        #                steps_cook='Приготовить тесто/Выложить яблоки/Запечь', time_cook='1 час', author='Admin')
        # recipe.save()
        # self.stdout.write(f'{recipe}')
        # name_categ = ['супы', 'горячие блюда', 'салаты', 'закуски', 'выпечки']
        # difficulty = ['легко', 'средне', 'сложно']
        # for i in name_categ:
        #     for j in difficulty:
        #         category = Categories(name_category=i, difficulty=j)
        #         category.save()
        #         self.stdout.write(f'{category}')
        # pk = kwargs.get('1')
        # for i in range(15):
        #     user = Categories.objects.first()
        #     if user is not None:
        #         user.delete()
        #     self.stdout.write(f'{user}')
        for i in range(5, int(Recipe.objects.latest('id').id) + 1):
            recipe = Recipe.objects.filter(pk=i).first()
            categ = Categories.objects.filter(pk=31)
            connect = Connection(recipe=recipe)
            connect.save()
            self.stdout.write(f'{connect}')
            for cat in categ:
                connect.categ_rec.add(cat)
            connect.save()
            self.stdout.write(f'{connect}')
