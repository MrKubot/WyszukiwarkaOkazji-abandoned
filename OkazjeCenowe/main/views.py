from urllib import request
from django.shortcuts import render, redirect
from . import forms
# Create your views here.

from bs4 import BeautifulSoup

from main.forms import FormularzDodawania
from main.models import DaneProduktu


def home(response):
    return render(response, 'main/home.html')


# użytkownik dodaje nazwe oraz linki do artykułu, który go interesuje
def dodaj(response):

    # jezeli uzytkownik wyslal formularz, dodawany jest nowy rekord do bazy danych
    if response.method == 'POST':
        nazwa = response.POST['nazwa']
        ULR_OLX = response.POST['URL_OLX']
        URL_CENEO = response.POST['URL_CENEO']
        URL_VINTED = response.POST['URL_VINTED']
        SCD = response.POST['SCD']

        nowy_produkt = DaneProduktu(nazwa=nazwa, URL_CENEO=URL_CENEO, URL_VINTED=URL_VINTED, ULR_OLX=ULR_OLX, SCD=SCD)
        nowy_produkt.save()

        return render(response, 'main/sukces.html')

    # jezeli uzytkownik dopiero wprowadza dane, zostanie mu wyswietlony formularz
    formularz = FormularzDodawania()

    return render(response, 'main/zapisz.html', {'form': formularz})


# uzytkownik dostanie aktualne ceny produktow
def wyszukanie(response):
    nazwa_podana = response.POST['wyszukane']
    
    dane_produktu = DaneProduktu.objects.get(nazwa=nazwa_podana)
    print(dane_produktu)

    soup_of_ceneo = BeautifulSoup('html', 'html.parser')
    soup_of_vinted = BeautifulSoup('html', 'html.parser')
    soup_of_olx = BeautifulSoup('html', 'html.parser')


    return render(response, 'main/znalezione.html')

