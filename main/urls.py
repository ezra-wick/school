from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('check/form/', views.check_form, name='check_form'),
    path('ajax/validfeeld/', views.check_feeld, name='valid_feeld')
]