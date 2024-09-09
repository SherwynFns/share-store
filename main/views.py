from django.shortcuts import render

def show_main(request):
    context = {
        'Application : Share Store'
        'name': 'A. Sherwyn Fawwaz',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)