from django.urls import path
from cheap.views import home

urlpatterns = [
    path('', home, name='home'),
]
