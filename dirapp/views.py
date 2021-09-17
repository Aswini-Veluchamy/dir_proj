from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def home (request):
    if request.method == "POST":
        username = request.POST['username']
        print(username)
        return render(request, "dirapp/home.html")
    else:
        return render(request, "dirapp/home.html")