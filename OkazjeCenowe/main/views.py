from urllib import request
from django.shortcuts import render, redirect
from . import forms
import requests
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
        URL_OLX = response.POST['URL_OLX']
        URL_CENEO = response.POST['URL_CENEO']
        URL_VINTED = response.POST['URL_VINTED']
        SCD = response.POST['SCD']

        nowy_produkt = DaneProduktu(nazwa=nazwa, URL_CENEO=URL_CENEO, URL_VINTED=URL_VINTED, URL_OLX=URL_OLX, SCD=SCD)
        nowy_produkt.save()

        print(nowy_produkt.nazwa)

        return render(response, 'main/sukces.html')

    # jezeli uzytkownik dopiero wprowadza dane, zostanie mu wyswietlony formularz
    formularz = FormularzDodawania()

    return render(response, 'main/zapisz.html', {'form': formularz})


# uzytkownik dostanie aktualne ceny produktow
def wyszukanie(response):
    nazwa_podana = response.POST['wyszukane']
    
    dane_produktu = DaneProduktu.objects.get(nazwa=nazwa_podana)

    r_ceneo = requests.get(dane_produktu.URL_CENEO)
    soup_of_ceneo = BeautifulSoup(r_ceneo.text, 'html.parser')

    r_vinted = requests.get(dane_produktu.URL_VINTED)
    soup_of_vinted = BeautifulSoup(r_vinted, 'html.parser')

    r_olx = requests.get(dane_produktu.URL_OLX)
    soup_of_olx = BeautifulSoup(r_olx, 'html.parser')
    

    ceny_ceneo, ceny_vinted, ceny_olx = najnizsza_cena(soup_ceneo=soup_of_ceneo, soup_olx=soup_of_olx, soup_vinted=soup_of_vinted)



    return render(response, 'main/znalezione.html')


def wszystkie(response):
    pass



def najnizsza_cena(soup_ceneo, soup_vinted, soup_olx):
    
    #Szukanie cen CENEO
    lista_produktow_ceneo = soup_ceneo.find(class_='category-list-body')

    ceny_ceneo = lista_produktow_ceneo.find_all(class_='value')
    same_ceny_ceneo = []
    for element in ceny_ceneo:
        same_ceny_ceneo.append(int(element.text))

    same_ceny_ceneo.sort()

    najlepsze_ceny_ceneo = same_ceny_ceneo[:4]
    #Szukanie cen VINTED


    

    #Szukanie cen OLX




    return najlepsze_ceny_ceneo, najlepsze_ceny_vinted, najlepsze_ceny_olx