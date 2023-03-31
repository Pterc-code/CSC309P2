from django.urls import path
from . import views


app_name = 'property'
urlpatterns = [
    path('', views.PropertyOverview, name='property'),
    path('create/', views.add_property, name='add-property'),
    path('view/<int:pk>/', views.view_property, name='view_property'),
    path('view/', views.view_propertyAll, name='view_Allproperty'),
    path('update/<int:pk>/', views.update_property, name='update_property'),
    path('delete/<int:pk>/', views.delete_property, name='delete-property'),
    path('search/<str:name>/<int:rating>/<int:price>/<int:bedroom>/<str:order_by_price>/<str:order_by_rating>/', views.search_property, name='search-property')
]