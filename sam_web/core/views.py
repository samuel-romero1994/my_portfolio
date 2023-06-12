from django.shortcuts import render, HttpResponse

# Create your views here.
"""
def home(request):
    return HttpResponse("<h1>Mi web personal</h1><h2>Portada</h2>")

def about(request):
    return HttpResponse("<h1>Mi web personal</h1><h2>About Me</h2>")

def portfolio(request):
    return HttpResponse("<h1>Mi web personal</h1><h2>Portafolio</h2>")

def contact(request):
    return HttpResponse("<h1>Mi web personal</h1><h2>Contáctame..</h2>")
"""

def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")

"""def portfolio(request):
    return render(request, "core/portfolio.html")"""

def contact(request):
    return render(request, "core/contact.html")