from django.urls import include, path
from rest_framework import routers
from backend import views


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api', views.MyProfile.as_view(), name='api'),
]