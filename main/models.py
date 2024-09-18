import uuid
from django.db import models

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nama = models.CharField(max_length=255)
    time = models.DateField(auto_now_add=True)
    deskripsi = models.TextField()
    stok = models.IntegerField()

    @property
    def is_mood_strong(self):
        return self.stok > 5