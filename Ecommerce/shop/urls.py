from django.urls import path
from .views import products_view, ProductListView, about, login_user, logout_user

app_name = 'shop'
urlpatterns = [
    path("",products_view, name='products_view'),
    # path("",ProductListView.as_view(), name='products_view'),
    path('about/', about, name='about'),
    path('login/', login_user , name='login'),
    path('logout/', logout_user, name='logout'),
]
