from django.contrib.auth.models import User
from django.db import models


class Note(models.Model):
    owner = models.ForeignKey(User, related_name="notes",
                              on_delete=models.CASCADE, null=True)
    text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
