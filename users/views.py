from django.shortcuts import render, redirect
from .models import User
from .forms import RegistrationForm
from django.core.mail import send_mail
import random

def send_otp(email):
    otp = random.randint(100000, 999999)
    send_mail(
        'Your OTP Code',
        f'Your OTP code is {otp}. Please use this to verify your account.',
        'noreply@datingapp.com',
        [email],
        fail_silently=False,
    )
    return otp

def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            otp = send_otp(user.email)
            request.session['otp'] = otp
            request.session['user_id'] = user.id
            return redirect('verify_otp')
    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', {'form': form})
