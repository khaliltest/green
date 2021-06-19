from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# Create your models here.

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class User(AbstractUser):
    full_name = models.CharField(max_length=50)
    image = models.ImageField(blank = True)
    created = models.DateTimeField(default = timezone.now)
    is_owner = models.BooleanField(default=False)
    is_advisor = models.BooleanField(default=False)
    number = models.IntegerField(default=0)
    code_agency = models.IntegerField(null=True, blank=True, default=0)




@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_tocken(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)