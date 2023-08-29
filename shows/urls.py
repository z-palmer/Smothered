from django.urls import path
from shows import views

app_name = 'shows'
urlpatterns = [

    # main views
    path('', views.index, name='index')

]
