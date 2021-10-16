from django.urls import path
from .views import home, createPerson,editPerson, detail, sertificat


urlpatterns = [
    path('',home,name='home'),
    path('add_person',createPerson,name='create'),
    path('<int:id>/edit',editPerson,name='edit'),
    path('<int:id>/detail',detail,name='detail'),
    path('<int:id>/sertificat',sertificat,name='sertificat'),




   
    
]