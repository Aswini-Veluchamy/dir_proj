from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def home (request):
    if request.method == "POST":
        username = request.POST['username']
        age = request.POST['age']
        salary = request.POST['salary']
        print(username,age,salary)
        return render(request, "dirapp/home.html")
    else:
        return render(request, "dirapp/home.html")