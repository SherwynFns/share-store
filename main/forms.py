from django.forms import ModelForm
from main.models import Product

class MoodEntryForm(ModelForm):
    class Meta:
        model = Product
        fields = ["nama", "deskripsi", "stok"]