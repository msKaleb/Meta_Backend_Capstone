# define URL route for index() view
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu', view=views.MenuView.as_view(), name='menu-view'),
    path('menu/<int:pk>', view=views.SingleMenuItemView.as_view(), name='menu-item-view'),
    path('api-token-auth', obtain_auth_token),
]
