from django.shortcuts import render
from apps.main.models import Main, Awards, About
# Create your views here.
def index(request):
    main = Main.objects.latest('id')
    return render(request, 'index.html', locals() )

def about(request):
    about = About.objects.latest("id")
    awards = Awards.objects.all()
    return render(request, 'about.html', locals() ) 

def contact(request):
    return render(request, 'contact.html', locals() ) 
