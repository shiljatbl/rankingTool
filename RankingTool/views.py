from django.shortcuts import render
from django.http import HttpResponse

def scraper(request):
    return render(request, "scraper.html", {})