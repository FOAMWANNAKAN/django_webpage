from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def card(request):
    return render(request, 'card.html')

def cardcolor(request):
    return render(request, 'cardcolor.html')

def form(request):
    return render(request, 'form.html')

def forpage(request):
    context = {}
    lt = list(range(1, 101))

    first_names = ["Alan", "Marckris", "Khunpol", "Heart", "Jinwook", "Thai", "Nex", "Phutatchai", "Copper", "AA", "Jungt", "Peemwasu"]
    last_names = ["Bus", "Bus", "Bus", "Bus", "Bus", "Bus", "Bus", "Bus", "Bus", "Bus", "Bus", "Bus"]
    handles = ["IG: Alan.bus", "IG: Marckris.bus", "IG: Khunpol.bus", "IG: Heart.bus", "IG: Jinwook.bus", "IG: Thai.bus", "IG: Nex.bus", "IG: Phutatchai.bus", "IG: Copper.bus", "IG: AA.bus", "IG: Jungt.bus", "IG: Peemwasu.bus"]

    data = []
    for i in lt:
        first_name = first_names[(i - 1) % len(first_names)]
        last_name = last_names[(i - 1) % len(last_names)]
        handle = handles[(i - 1) % len(handles)]
        data.append({
            "id": i,
            "first_name": first_name,
            "last_name": last_name,
            "handle": handle
        })

    context["list"] = data

    return render(request, 'forpage.html', context)


