from loja.views import index
from django.urls import path

app_name = 'loja'

urlpatterns = [
    path('', index, name='index'),
]