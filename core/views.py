from django.shortcuts import render, reverse, redirect
from .models import User, Products
# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            return render(request, 'core/register.html', {
                'error':1
            })
        user_data = User(username=username, password=password)
        user_data.save()
        return render(request, 'core/home.html')
    
    else:    
        return render(request, 'core/register.html')
    
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try: 
            user = User.objects.get(username=username)
            if user.password == password:
                request.session['user_id'] = user.id
                request.session['username'] = user.username
                return render(request, 'core/home.html')
        except User.DoesNotExist:
            pass            
        return render(request, 'core/login.html')
    return render(request, 'core/login.html')

def feautures(request):
    return render(request, 'core/features.html')

def store(request):
    products = Products.objects.all()
    return render(request, 'core/store.html', {
        'products': products
    })
            