from django.urls import path
from .views import *

app_name = 'shop'
urlpatterns = [
    path("",products_view, name='products_view'),
    # path("",ProductListView.as_view(), name='products_view'),
    path('about/', about, name='about'),
    path('login/', login_user , name='login'),
    path('logout/', logout_user, name='logout'),
    path('product/<int:pk>', product, name='product'),
    path('category/<str:cat>', category, name='category'),
    path('category/', category_summary, name='category_summary'),
]
