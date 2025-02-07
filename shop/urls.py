from django.urls import path
from .import views

urlpatterns = [
    path('', views.home,name='home'),
    path('menu', views.menu,name='menu'),
    path('detail/<int:tea_id>', views.teadetail,name='teadetail'),
    path('aboutus', views.aboutus,name='aboutus'),
    path('loca', views.loca,name='loca'),
    path('thank', views.thank,name='thank'),
]