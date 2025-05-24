from django.urls import  path
from .views import *
urlpatterns = [
   ## path("product",all_products,name="all_products"),
    #path("product/<str:pk>",get_product_by_id,name="get_product_by_id"),
    #path("products/",get_product_by_filter,name="get_product_by_filter"),
    path("api/regester",sign_up,name="sign"),
    path("api/log_in",log_in,name="log_in"),
    path("api/create_post",create_post,name="create_post"),



    


]