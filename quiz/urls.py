from django.urls import path
from quiz import views

app_name = 'quiz'
urlpatterns = [

    # main views
    path('', views.index, name='index')

]
