from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request, 'balanced_diet/index.html')

@login_required
def my_diet(request):
    return render(request, 'balanced_diet/my_diet.html')
