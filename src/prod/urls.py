from django.urls import path
from .views import product_details_view, product_create_view, product_create_view2, \
    modify_data_view, dynamic_content_lookup, delete_object, queryDisplyAll

app_name = "prod"

urlpatterns=[
    path('', product_details_view, ),
    path('create/', product_create_view, ),
    path('create2/', product_create_view2, ),
    path('modify/', modify_data_view, ),
    path('<int:id>/', dynamic_content_lookup, name="particularProd" ),
    path('<int:id>/delete', delete_object, name="delete" ),
    path('all/', queryDisplyAll, name="all" ),
]
