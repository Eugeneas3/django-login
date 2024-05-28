from django.urls import include, path
from . import views


urlpatterns = [
    path('',views.index, name='index'),
    path('djangologin/', views.djangologin, name='djangologin')
]