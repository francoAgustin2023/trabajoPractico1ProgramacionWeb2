from django.shortcuts import render
from .models import Mensaje

def mensajes_filtrados(request, filtro):
    if filtro is None:
        filtro = 'ninguno'

    if filtro == 'remitente':
        mensajes = Mensaje.objects.filter(remitente="Juan")
        filtro_actual = "Filtrado por remitente"
    elif filtro == 'destinatario':
        mensajes = Mensaje.objects.filter(remitente="Maria")
        filtro_actual = "Filtrado por destinatario"
    elif filtro == 'ninguno':
        mensajes = Mensaje.objects.all()
        filtro_actual = "Ninguno (Se muestran todos)"
    else:
        return render(request, '404.html', status=404)

    return render(request, 'mensajes/mensajes_filtrados.html', {'mensajes': mensajes, 'filtro_actual': filtro_actual})
