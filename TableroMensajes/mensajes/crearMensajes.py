#Este va a ser el script de creacion de instancias de mensajes en la base de datos

#Se debe copiar todo esto y ejecutarse en la Python Shell, dentro del entorno y de esta forma:
#python manage.py shell

#Se crean 10 mensajes, simulando una conversacion entre dos personas: Juan y Maria

from mensajes.models import Mensaje

mensajes = [
    Mensaje(texto="Hola como estas? Yo estoy trabajando", remitente="Juan", destinatario="Maria"),
    Mensaje(texto="Hola! Que bueno, yo estoy en la universidad.", remitente="Maria", destinatario="Juan"),
    Mensaje(texto="Hoy es un dia bastante agotador!", remitente="Juan", destinatario="Maria"),
    Mensaje(texto="Si, ademas hay que planificar los viajes del fin de semana.", remitente="Maria", destinatario="Juan"),
    Mensaje(texto="Es cierto! Yo ya reserve los pasajes", remitente="Juan", destinatario="Maria"),
    Mensaje(texto="Que bueno! Acordate de todas las cosas que debemos llevar.", remitente="Maria", destinatario="Juan"),
    Mensaje(texto="Si! Para no olvidarme voy a hacer una lista.", remitente="Juan", destinatario="Maria"),
    Mensaje(texto="Bien! De esa forma entonces todo va a salir bien", remitente="Maria", destinatario="Juan"),
    Mensaje(texto="Asi es! Bueno que tengas un buen dia en la universidad. Nos vemos!", remitente="Juan", destinatario="Maria"),
    Mensaje(texto="Igualmente en tu trabajo! Adios!", remitente="Maria", destinatario="Juan"),
]

for mensaje in mensajes:
    mensaje.save()

exit()
