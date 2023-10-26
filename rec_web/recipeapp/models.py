from django.db import models


class Recipe(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    ingredients = models.TextField()
    steps_cook = models.TextField()
    time_cook = models.CharField(max_length=20)
    author = models.CharField(max_length=50)
    image = models.ImageField(default=None)

    def __str__(self):
        return f'{self.title}, {self.description}'


class Categories(models.Model):
    name_category = models.CharField(max_length=30)
    difficulty = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.name_category}, {self.difficulty}'


class Connection(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    categ_rec = models.ManyToManyField(Categories)

    def __str__(self):
        return f'{self.recipe}, {self.categ_rec}'
