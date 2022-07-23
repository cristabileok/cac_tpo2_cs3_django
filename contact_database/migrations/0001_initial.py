# Generated by Django 4.0.6 on 2022-07-21 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Nombre')),
                ('age', models.FloatField(max_length=3, verbose_name='Edad')),
                ('sex', models.CharField(choices=[('ma', 'Male'), ('fe', 'Female')], max_length=2, verbose_name='Sexo')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('phone', models.IntegerField(verbose_name='Número de Teléfono')),
                ('comunication', models.CharField(choices=[('EMA', 'Email'), ('WAS', 'Whatsapp'), ('SMS', 'Mensaje de Texto'), ('TEL', 'Telegram')], default='WAS', max_length=3, verbose_name='Canal de comunicación preferido')),
                ('reason', models.CharField(choices=[('FIT', 'Quiero mejorar mi condición física'), ('SPO', 'Soy deportista y quiero mejorar mi rendimiento'), ('PAI', 'Sufro de dolor o lesiones')], max_length=3, verbose_name='Motivo de la Consulta')),
                ('message', models.TextField(verbose_name='Mensaje')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Última Modificación')),
            ],
        ),
    ]