# define URL route for index() view
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu', view=views.MenuView.as_view(), name='menu_view'),
    path('menu/<int:pk>', view=views.SingleMenuItemView.as_view(), name='menu_item_view'),
]
