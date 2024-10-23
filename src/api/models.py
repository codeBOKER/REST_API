from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class Book(models.Model):
    name= models.CharField(_("book name"), max_length=50)
    user= models.ForeignKey(User, verbose_name=_("user"), on_delete=models.CASCADE)
    auther= models.CharField(_("author"), max_length=50)
    date=models.DateField(_("daate"),  auto_now_add=True)

    def __str__(self):
        return self.name
    

