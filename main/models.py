from django.db import models

class Product(models.Model):
    nama = models.CharField(max_length=255)
    kategori = models.CharField(max_length=255)
    deskripsi = models.TextField()
    stok = models.IntegerField()
    harga = models.IntegerField()

    @property
    def is_mood_strong(self):
        return self.mood_intensity>5
    

