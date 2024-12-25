from django.urls import path
from apps.main.views import index, about

urlpatterns = [
    path('', index, name='index')
]

urlpatterns =[
    path('', about, name='about')
]
