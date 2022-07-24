from django.urls import path
from .models import Reservation
from. import views

app_name = 'reservation'
urlpatterns = [
    path('',views.reserve_table,name="reserve_table"),
  
]