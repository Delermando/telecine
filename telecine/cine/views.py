from django.shortcuts import render

def home( request ):
    context = {'texto': 'Seu primeiro projeto em Django'}
    return render(request, 'index.html', context)