from django.db import models

# Create your models here.

class TOPIC(models.Model):
    
    title = models.CharField(max_length=255, null=True, blank=True)

    body = models.TextField(null=True, blank=True)

    create_date = models.DateTimeField(null=True, default=None)

    update_date = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']
