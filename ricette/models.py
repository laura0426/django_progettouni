
from django.db import models
from django.contrib.auth.models import User, PermissionsMixin, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        user = User.objects.create_user(username, password)
        if not username:
            raise ValueError('The given username must be set')

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        return self.create_user(username, password, **extra_fields)

class Ricette(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    nome = models.CharField(max_length=30)
    ingredienti = models.CharField(max_length=30)
    procedimento = models.CharField(max_length=30)
    tempo = models.CharField(max_length=30)
    difficolta = models.CharField(max_length=30)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE, null=True)



class Categoria(models.Model):
    nome = models.CharField(max_length=30, primary_key=True, unique=True)

class Preferiti(models.Model):
    lista=models.ManyToManyField(Ricette)
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True)