from django.urls import path
from shop import views

app_name = 'shop'
urlpatterns = [

    # main views
    path('', views.index, name='index')

]
