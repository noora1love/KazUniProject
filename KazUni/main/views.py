from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    user = User.objects.all()
    return render(request, 'main/index.html', {'User': User})
