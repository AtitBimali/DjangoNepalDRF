from django.urls import path
from . import views
from django.conf import settings
 
urlpatterns = [
path('', views.getAll,name='home'),
path('province/', views.getProvince,name='province'),
path('district/', views.getDistrict,name='district'),
path('municipality/', views.getMunicipality,name='municipality'),
path('html-view/',views.html_view,name='html-view')
]