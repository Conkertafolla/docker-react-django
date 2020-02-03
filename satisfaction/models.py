from django.db import models
from django import forms

#Modelo para la tabla usuario
class User(models.Model):
    #Tipos de roles 
    ADMINISTRATOR_ROLE = 'ADMIN'
    USER_ROLE = 'USER'
    ROLE_TYPE = {
        (ADMINISTRATOR_ROLE, 'Administrator'),
        (USER_ROLE, 'User')
    }

    #Estatus de los usuarios
    BLOCKED = 'BLOCKED'
    ACTIVE = 'ACTIVE'
    NEW = 'NEW'
    USER_STATUS = {
        (BLOCKED, 'BLOCKED'),
        (NEW, 'NEW'),
        (ACTIVE, 'ACTIVE')
    }

    user_id = models.IntegerField(primary_key = True)
    user_name = models.CharField(max_length = 100)
    user_lastname = models.CharField(max_length = 100)
    nickname = models.CharField(max_length = 100)
    password = forms.CharField(widget = forms.PasswordInput)
    email = models.EmailField(unique = True)
    role = models.CharField( max_length = 100, choices = ROLE_TYPE)
    last_connection = models.DateTimeField(auto_now = True)
    status = models.CharField(max_length = 100, choices = USER_STATUS)


