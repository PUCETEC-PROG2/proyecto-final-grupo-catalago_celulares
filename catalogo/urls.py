from django.urls import path
from . import views
app_name = 'catalogo'

urlpatterns = [
    path('customer/list/', views.customer_list, name='customer_list'),
    path('customer/add/', views.customer_add, name='customer_add'),
    path('', views.index, name='index'),
    path('customer/', views.customer, name='customer'),
    path('customer/<int:customer_id>/', views.info_customer, name='info_customer'),
    path('customer/add/', views.add_customer, name='add_customer'),
    path('customer/<int:id>/edit/', views.edit_customer, name='edit_customer'),
    path('customer/<int:id>/delete/', views.delete_customer, name='delete_customer'),
    path('category/', views.category, name='category'),
    path('category/<int:category_id>/', views.info_category, name='info_category'),
    path('category/add/', views.add_category, name='add_category'),
    path('category/<int:id>/edit/', views.edit_category, name='edit_category'),
    path('category/<int:id>/delete/', views.delete_category, name='delete_category'),
    path('product/', views.product, name='product'),
    path('product/<int:product_id>/', views.info_product, name='info_product'),
    path('product/add/', views.add_product, name='add_product'),
    path('product/<int:id>/edit/', views.edit_product, name='edit_product'),
    path('product/<int:id>/delete/', views.delete_product, name='delete_product'),
    path('sale/', views.sale, name='sale'),
    path('sale/<int:sale_id>/', views.info_sale, name='info_sale'),
    path('sale/add/', views.add_sale, name='add_sale'),
    path('add_saleproduct/<int:product_id>/', views.add_saleproduct, name='add_saleproduct'),
]
