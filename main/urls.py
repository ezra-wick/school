from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('check/form/', views.check_form, name='check_form'),
    path("start_bot/", views.start_bot, name="start_bot"),
    path('ajax/validfeeld/', views.check_feeld, name='valid_feeld')
]