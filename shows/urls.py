from django.urls import path
from shows import views

urlpatterns = [

    # main views
    path('', views.index, name='index')

]
