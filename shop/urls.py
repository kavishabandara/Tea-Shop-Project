from django.urls import path
from .import views

urlpatterns = [
    path('', views.home,name='home'),
    path('menu', views.menu,name='menu'),
    path('detail/<int:tea_id>', views.teadetail,name='teadetail'),
]