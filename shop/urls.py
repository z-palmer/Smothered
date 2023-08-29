from django.urls import path
from shop import views

urlpatterns = [

    # main views
    path('', views.index, name='index')

]
