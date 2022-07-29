from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=30, verbose_name="Nombre")
    age = models.FloatField(max_length=3, verbose_name="Edad")
    
    ch_male = 'ma'
    ch_female = 'fe'
    sex_choice = [(ch_male,"Hombre"), (ch_female,"Mujer")]
    sex = models.CharField(max_length=2, choices=sex_choice, verbose_name="Sexo")
    
    email = models.EmailField(verbose_name="Email")
    phone = models.IntegerField(verbose_name="Número de Teléfono")
    
    ch_email = "EMA"
    ch_wapp = "WAS"
    ch_sms = "SMS"
    ch_telegram = "TEL"
    comunication_choice = [
        (ch_email, "Email"),
        (ch_wapp, "Whatsapp"),
        (ch_sms, "Mensaje de Texto"),
        (ch_telegram, "Telegram")
        ]
    comunication = models.CharField(max_length=3, choices=comunication_choice, default=ch_wapp, verbose_name="Canal de comunicación preferido")
    
    
    ch_fitness = "FIT"
    ch_sport = "SPO"
    ch_pain = "PAI"
    reason_choice = [
        (ch_fitness, "Quiero mejorar mi condición física"),
        (ch_sport, "Soy deportista y quiero mejorar mi rendimiento"),
        (ch_pain, "Sufro de dolor o lesiones")
    ]
    reason = models.CharField(max_length=3, choices=reason_choice, verbose_name="Motivo de la Consulta")
    
    message = models.TextField(verbose_name="Mensaje")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Última Modificación")
          
    
def __str__(self):
    return self.name

class Meta:
    verbose_name = "Contacto"
    verbose_name_plural = "Contactos"
    ordering = ["-created"]
    
    