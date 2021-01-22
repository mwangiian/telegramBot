from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('telBot/', views.telBot, name='telBot'),

]