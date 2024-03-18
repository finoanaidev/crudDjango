from django.db import models

#user ->id(AutoField), name(CharField), age(IntegerField)

# Create your models here.

# class User(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=255)
#     gender = models.CharField(max_length=10)
#     age = models.IntegerField()

class User(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=225)
    prenom = models.CharField(max_length=255)
    mail = models.EmailField()
    telephone = models.CharField(max_length=20, help_text="Format: +1234567890")
    copropriete_gere = models.CharField(max_length = 200)