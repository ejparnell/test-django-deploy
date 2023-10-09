from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cats/', views.cats_index, name='index'),
    # <int:var_name> - Since the urls params will always be strings. We can use the built in
    # converter to change that string to an int
    path('cats/<int:cat_id>/', views.cat_detail, name='detail'),
]