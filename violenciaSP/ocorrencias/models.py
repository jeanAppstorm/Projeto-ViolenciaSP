from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Delegacias(models.Model):

    nome = models.CharField(max_length=50)
    endereço = models.CharField(max_length=100)


class Dados(models.Model):

    MESES = (
        ("Jan","Janeiro"),
        ("Fev","Feveireiro"),
        ("Mar","Março"),
        ("Abr","Abril"),
        ("Mai","Maio"),
        ("Jun","Junho"),
        ("Jul","Julho"),
        ("Ago","Agosto"),
        ("Set","Setembro"),
        ("Out","Outubro"),
        ("Nov","Novembro"),
        ("Dez","Dezembro")
    )


    ano = models.IntegerField(
        validators=[
            MinValueValidator(2001),
            MaxValueValidator(2100)
        ]
    )

    mes = models.CharField(
        max_length=3,
        choices=MESES
    )
