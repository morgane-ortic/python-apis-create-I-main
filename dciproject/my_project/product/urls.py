from django.urls import include, path
from customer.views import GetCreateProductView, ProductListByNameView, ProductRetrieveDestroyView

app_name = 'product'

urlpatterns = [ 
    path('products/', GetCreateProductView.as_view(), name='product-list-create'),
    path('products/<str:name>/', ProductListByNameView.as_view(), name='product-list-by-name'),
    path('products/<int:pk>/', ProductRetrieveDestroyView.as_view(), name='product-retrieve-destroy'),
]