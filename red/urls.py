from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('fav/',views.fav,name='fav'),
    path('fav/log/',views.log,name="log"),
]