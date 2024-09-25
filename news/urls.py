from django.contrib import admin
from django.urls import path 
from .views import *


urlpatterns = [
path('category/', CategoryView.as_view()),
path('categoryname/', CategoryNameView.as_view()),
path('news/',NewsView.as_view()),
path('category/<int:id>/', CategoryDetailAPIView.as_view(),),
path('news/<int:id>/', NewsDetailAPIView.as_view(),),
]

#  <Link to={`/product/${product.id}`}><Card.Header>{product.title}</Card.Header></Link>
#  <Route path="/product/:id" component={ProductDetail} />
# path('product/<pk>/', ItemDetailView.as_view() , name='product-detail' ),