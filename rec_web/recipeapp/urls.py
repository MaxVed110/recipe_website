from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
                  path('', views.index, name='index'),
                  path('base_recipe/<int:recipe_id>/', views.base_rec, name='base_rec'),
                  path('all_recipe/', views.all_recipe, name='all_recipe'),
                  path('add_recipe/', views.add_recipe, name='add_recipe'),
                  path('about/', views.about, name='about'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
