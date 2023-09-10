from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length = 300)
    last_name = models.CharField(max_length = 300)
    email = models.CharField(max_length = 300)

    def __str__(self):
        return self.first_name