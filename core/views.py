from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")

def timetable_fees(request):
    return render(request, "core/timetable_fees.html")

