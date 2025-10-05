from django.db import models

class Credential(models.Model):
    app_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    url = models.URLField(blank=True)

    def __str__(self):
        return f"{self.app_name} - {self.username}"


