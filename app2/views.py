from django.shortcuts import render

# Create your views here.
def third(request):
    return render(request,'third.html')
def four(request):
    return render(request,'four.html')