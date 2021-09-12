from django.conf.urls import url, include
from rest_framework import routers
from django.urls import path
from .views import ApiDemo

app_name='backend'
router = routers.DefaultRouter()
urlpatterns = [
    url(r'api/v1/apidemo/', ApiDemo.as_view(), name="apidemo")
]
