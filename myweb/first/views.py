
from django.views.generic import ListView
from django.shortcuts import render
from .models import Index
# Create your views here.
class IndexPageView(ListView):
    model=Index
    template_name='index.html'
