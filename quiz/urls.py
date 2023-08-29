from django.urls import path
from quiz import views

urlpatterns = [

    # main views
    path('', views.index, name='index')

]
