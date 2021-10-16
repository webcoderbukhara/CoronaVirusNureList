from django.urls import path
from .views import sign_up, sign_in,logout_view

urlpatterns = [
    path('sign_up/',sign_up,name='up'),
    path('sign_in/',sign_in,name='in' ),
    path('logout/',logout_view,name='logout'),
   
    
]
