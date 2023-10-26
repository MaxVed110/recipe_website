from django import forms


class AddRecipeForm(forms.Form):
    title = forms.CharField(label='Название', max_length=50,
                            widget=forms.TextInput(
                                attrs={'class': 'input_char', 'placeholder': 'Введите краткое название блюда'}))
    description = forms.CharField(label='Описание',
                                  widget=forms.Textarea(
                                      attrs={'class': 'input_area', 'placeholder': 'Введите краткое описание рецепта'}))
    ingredients = forms.CharField(label='Ингридиенты', widget=forms.Textarea(
        attrs={'class': 'input_area', 'placeholder': 'Введите ингридиенты, разделяя из символом "/"'}))
    steps_cook = forms.CharField(label='Шаги приготовления', widget=forms.Textarea(
        attrs={'class': 'input_area', 'placeholder': 'Введите шаги приготовления, каждый шаг разделяя символом "/"'}))
    time_cook = forms.CharField(label='Время приготовления', max_length=20,
                                widget=forms.TextInput(
                                    attrs={'class': 'input_char', 'placeholder': 'Введите время приготовления'}))
    author = forms.CharField(label='Автор', max_length=50,
                             widget=forms.TextInput(attrs={'class': 'input_char', 'placeholder': 'Введите имя автора'}))
    image = forms.ImageField(label='Изображение', )
    category = forms.ChoiceField(label='Категория',
                                 choices=[('супы/легко', 'Супы Легко'), ('супы/средне', 'Супы Средне'),
                                          ('супы/сложно', 'Супы Сложно'),
                                          ('горячие блюда/легко', 'Горячие блюда Легко'),
                                          ('горячие блюда/средне', 'Горячие блюда Средне'),
                                          ('горячие блюда/сложно', 'Горячие блюда Сложно'),
                                          ('салаты/легко', 'Салаты Легко'), ('салаты/средне', 'Салаты Средне'),
                                          ('салаты/сложно', 'Салаты Сложно'), ('закуски/легко', 'Закуски Легко'),
                                          ('закуски/средне', 'Закуски Средне'), ('закуски/сложно', 'Закуски Сложно'),
                                          ('выпечки/легко', 'Выпечки Легко'), ('выпечки/средне', 'Выпечки Средне'),
                                          ('выпечки/сложно', 'Выпечки Сложно')])
