from django.shortcuts import render
from meals.models import Meals



# Create your views here.
def home(request):
    meals=Meals.objects.all()
    meal_list=Meals.objects.all()
    context={ 'meals': meals,'meal_list':meal_list


    }

    return render(request,'index.html',context)