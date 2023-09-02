from django.urls import path
from main import views
urlpatterns = [
    path('',views.index, name='index'),
    path('data_collection',views.data_collection, name='data_collection'),
     
 ]
 