from django.urls import path
from . import views

urlpatterns = [
    path('', views.revcomments_list),

]
