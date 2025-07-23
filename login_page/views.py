from django.shortcuts import render, redirect
from django.contrib import messages
from .firebase_config import auth
import requests
import os
from dotenv import load_dotenv
load_dotenv()
# Create your views here.
def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = auth.create_user(email=email, password=password)
            messages.success(request, 'Account created successfully!')
            return redirect('signin')
        except Exception as e:
            messages.error(request, f'Error: {e}')
    return render(request, 'login_page/signup.html')

def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        import requests
        api_key = os.getenv('FIREBASE_WEB_API_KEY')
        url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={api_key}"
        payload = {
            "email": email,
            "password": password,
            "returnSecureToken": True
        }
        r = requests.post(url, data=payload)
        data = r.json()
        if r.status_code == 200 and 'idToken' in r.json():
            request.session['firebase_user'] = {
                "email":      data["email"],
                "idToken":    data["idToken"],
                "refreshToken": data["refreshToken"],
            }
            # Successful sign in
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'login_page/signin.html')

def dashboard(request):
    user = request.session.get('firebase_user')
    if not user:
        # Not logged in → send them back to sign‑in
        return redirect('signin')

    # Now we know it exists
    user_email = user.get('email')
    print(user_email)
    return render(request, 'login_page/dashboard.html', {'user_email': user_email})

def home(request):
    pass

def find_bar(request):
    pass

def host_bar(request):
    pass

def friends(request):
    pass