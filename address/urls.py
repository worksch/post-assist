from django.conf.urls import  url
from django.urls import path

from . import views

app_name = 'address'

# RESTfull Framework
urlpatterns = [
    #url(r'^api/$', views.AddressView.as_view(), name='address'),
    #path('address/', views.address_list, name='address'),
    path('address/', views.StudentAddressView.as_view(), name='address'),
    path('address/<int:id>', views.StudentAddressView.as_view(), name='address'),
]