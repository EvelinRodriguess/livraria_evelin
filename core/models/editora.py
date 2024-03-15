from django.db import models 

class Editora(models.Model):
    nome = models.Charfield(max_length=100)
    url = model.URLField(max_length=200, blank=true, null=true)
    