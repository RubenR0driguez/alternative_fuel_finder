from django.urls import path
from . import views

urlpatterns = [
    path('', views.newlocations_list),

]
