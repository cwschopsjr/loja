from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
def index(request):
    return render(
        request,
        'loja/pages/index.html'
    )