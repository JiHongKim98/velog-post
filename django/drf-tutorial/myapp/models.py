from django.db import models

from django.db import models

class testdb(models.Model):
    charFields1 = models.CharField(max_length=10, default="hi1")
    charFields2 = models.CharField(max_length=20, default="hi2")
    content = models.TextField()