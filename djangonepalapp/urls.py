from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register("province",views.ProvinceViewSet)
router.register("district",views.DistrictViewSet)
router.register("municipality",views.MunicipalityViewSet)


router_urls = [
    path("", include(router.urls)),
]

urlpatterns = [
path('home/',views.html_view,name='home')
]

urlpatterns += router_urls

