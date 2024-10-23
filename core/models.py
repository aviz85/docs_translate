from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Document(models.Model):
    title = models.CharField(max_length=255)
    original_file = models.FileField(upload_to='documents/original/')
    translated_file = models.FileField(upload_to='documents/translated/', null=True, blank=True)
    source_language = models.CharField(max_length=50)
    target_language = models.CharField(max_length=50)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('in_progress', 'In Progress'),
            ('completed', 'Completed'),
            ('failed', 'Failed')
        ],
        default='pending'
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
