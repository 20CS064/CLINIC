from django.contrib import admin
from . import views
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register('patient',views.PatientView)


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.login , name = "login"),
    path('login',views.registration,name="registration"),
    path('',include(router.urls)),
    # path('api-auth/', include('rest_framework.urls'))
]