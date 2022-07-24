from django.shortcuts import render
from .forms import *
from .models import *

from reservation.models import Reservation

# Create your views here.
def reserve_table(request):
    reserve_form= ReserveTableForm()

    if request.method=="POST":
        reserve_form=ReserveTableForm(request.POST)

        if reserve_form.is_valid:
            reserve_form.save()
    context={'form':reserve_form}
    
    return render(request,'reservation.html',context)