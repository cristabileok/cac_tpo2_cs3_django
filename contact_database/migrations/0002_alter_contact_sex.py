# Generated by Django 4.0.6 on 2022-07-29 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_database', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='sex',
            field=models.CharField(choices=[('ma', 'Hombre'), ('fe', 'Mujer')], max_length=2, verbose_name='Sexo'),
        ),
    ]
