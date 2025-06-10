from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm
from django.contrib.auth import logout
from django.contrib import messages

def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        try:
            form.save()
            messages.success(request, "Registration successful! Please log in.")
            return redirect('login')  # Redirect to login page after registration
        except Exception as e:
            # If user already exists or any other error
            messages.error(request, "User already exists. Please try to log in.")
            return redirect('register')
    return render(request, 'registration/register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('customer_dashboard')

    form = LoginForm(request, data=request.POST or None)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('customer_dashboard')
    else:
        if request.method == 'POST':
            messages.error(request, 'Invalid username or password.')

    return render(request, 'registration/login.html', {'form': form})



def logout_view(request):
    logout(request)
    return redirect('login')



from .models import Shipment, Refund, Payment, Wallet, FXTransaction

from .forms import UserProfileForm

from .forms import UserProfileForm  # already updated

@login_required
def customer_dashboard(request):
    user = request.user
    shipments = Shipment.objects.filter(user=user)
    refunds = Refund.objects.filter(user=user)
    payments = Payment.objects.filter(user=user)
    wallet = Wallet.objects.filter(user=user).first()
    fx_transactions = FXTransaction.objects.filter(user=user)

    show_form = request.GET.get('edit') == '1'

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('customer_dashboard')  # redirect to avoid resubmission
    else:
        form = UserProfileForm(instance=user)

    context = {
        'shipments': shipments,
        'refunds': refunds,
        'payments': payments,
        'wallet': wallet,
        'fx_transactions': fx_transactions,
        'form': form,
        'show_form': show_form,
    }
    return render(request, 'finance/dashboard.html', context)
