from django.shortcuts import render
from cars.models import Car

def cars_view(request):
    cars = Car.objects.all().order_by('model')
    search = request.GET.get('search')
    
    if search:
        cars = Car.objects.filter(model='Camaro')
        
    
    return render(request,
                  'cars.html',
                  {'cars':cars }
                  )