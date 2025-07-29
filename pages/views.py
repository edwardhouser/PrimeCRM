from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, "home.html")

def features_view(request):
    return render(request, "features.html")

def pricing_view(request):
    return render(request, "pricing.html")

