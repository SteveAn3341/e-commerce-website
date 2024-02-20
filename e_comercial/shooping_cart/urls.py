from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name = 'home'),
    path('category/<int:category_id>/', views.category, name='category'),
    path('product/', views.product, name='product'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
    path('personal_use/',views.personal_use, name = 'personal_use'),
    path('office_use/',views.office_use, name = 'office_use'),
    path('home_use/',views.home_use, name = 'home_use'),
    path('shopping_cart/',views.shopping_cart, name='shopping_cart'),
    path('add_to_cart/<int:product_id>/',views.add_to_cart, name ='add_to_cart'),
    path('remove_from_cart/<int:product_id>/',views.remove_from_cart,name= 'remove_from_cart'),


]
