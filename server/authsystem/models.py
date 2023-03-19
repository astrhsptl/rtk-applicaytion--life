import jwt
import uuid
from django.db import models
from django.conf import settings
from django.urls import reverse_lazy
from datetime import datetime, timedelta
from django.contrib.auth.models import (
	AbstractBaseUser, BaseUserManager,
)


class UserManager(BaseUserManager):
    def create_user(self, name, surname, username, email, password, status, itn, **kwargs):
        if email is None:
            raise TypeError('Users must have an email address.')
        
        if password is None:
            raise TypeError('Users must have an email address.')

        user = self.model(email=self.normalize_email(email))
        user.name = name
        user.itn = itn
        user.surname = surname
        user.status = status
        user.username = username
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, username, password, status, name='asd', surname='asd', **kwargs):
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(name='asd', surname='asd', username=username, email=email, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.private_access = True
        user.status = UserStatus.objects.get(pk=2)
        user.name = name
        user.surname = surname
        user.username = username
        user.save()

        return user

class UserStatus(models.Model):
    title = models.CharField(max_length=64, unique=True)

    class Meta:
        verbose_name = ("User Status")
        verbose_name_plural = ("User Statuses")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy("user_status_detail", kwargs={"pk": self.pk})


class User(AbstractBaseUser):
    id = models.UUIDField(
        primary_key=True,
        db_index=True,
        default=uuid.uuid4,
        editable=False
    )
    
    email = models.EmailField(max_length=256, unique=True)
    username = models.CharField(max_length=256, unique=True)

    cyc = models.IntegerField(null=True, blank=True, unique=True)
    itn = models.IntegerField(null=True, blank=True, unique=True)  # individual tax number 

    name = models.CharField(max_length=64, blank=True, null=True)
    surname = models.CharField(max_length=64, blank=True, null=True)
    
    status = models.ForeignKey(UserStatus, on_delete=models.PROTECT)
    
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False) 
    is_staff = models.BooleanField(default=False)

    # Auth settings
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'username'
    ]

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    def get_absolute_url(self,):
        return reverse_lazy('moder_user_detail', kwargs={'id': self.id})