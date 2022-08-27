from django.shortcuts import render
import random


def home(request):

    return render(request, 'generador/home.html', {})


def about(request):

    return render (request, 'generador/about.html', {})


def password(request):

    letras = list('abcdefghijklmnopqrstuvwxyz')
    generar_password = ''

    longitud = int(request.GET.get('longitud'))

    if request.GET.get('mayusculas'):
        letras.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('simbolos'):
        letras.extend(list('!"#$%&()*+,-./:;<=>/?@[\]^_`{|}~'))
    if request.GET.get('numeros'):
        letras.extend(list('1234567890'))

    for letra in range(longitud):
        generar_password += random.choice(letras)

    return render (request, 'generador/password.html', {'password': generar_password})

