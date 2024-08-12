from django.shortcuts import render
from .models import Section

def home_view(request):
    section = Section.objects.get(title="Home")
    return render(request, 'home.html', {'section': section})

def about_view(request):
    section = Section.objects.get(title="About")
    return render(request, 'about.html', {'section': section})