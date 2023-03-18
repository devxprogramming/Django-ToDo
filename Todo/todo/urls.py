from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('complete/<todo_id>', views.completeTodo, name='complete'),
    path('deletecompleted/', views.deletecompleted, name='deletecompleted'),
    path('deletall/',views.deletall, name='deletall')
]
