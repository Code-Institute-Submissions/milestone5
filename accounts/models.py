from django.db import models
from django.contrib.auth import get_user_model

class Token(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    
    def __str__(self):
        return "{0} {1}".format(self.user, self.amount)