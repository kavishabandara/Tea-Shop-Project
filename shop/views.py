from django.shortcuts import render
from .models import tea


def home(request):
    favotea = tea.objects.filter(id__in=[1, 3, 5])
    return render (request,'home.html',{
        'favtea':favotea
    })

def menu(request):
    tealist=tea.objects.all()
    return render (request,'menu.html',{
        'tealist': tealist
    })
def teadetail(request,tea_id):
    teap=tea.objects.get(id=tea_id)
    variants = ["100g - Rs.1000", "250g - Rs.2500", "500g - Rs.4500", "1kg - Rs.8000"]
    return render(request,'teadetail.html',{
        'teap':teap,
        'variants': variants

    })
def aboutus(request):
    return render (request,'aboutus.html')
def loca(request):
    return render (request,'location.html')
def thank(request):
    return render (request,'thanks.html')