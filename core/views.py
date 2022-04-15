from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')


def carrier_page(request):
    return render(request,'home.html')

def client_page(request):
    return render(request,'home.html')