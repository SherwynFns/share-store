from django.shortcuts import render

def show_main(request):
    context = {
        'NamaItem' : 'Kaos Oversize',
        'Kategori': "Men's Tops",
        'Deskripsi': 'Kaos viral dengan bahan katun yang sangat nyaman dipakai',
        'Stok' : '10',
        'Harga' : 'Rp 50.000',
    }

    return render(request, "main.html", context)