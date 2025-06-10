# trnx/urls.py
from django.contrib import admin
from django.urls import path, include
from finance import views as finance_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', finance_views.register_view, name='register'),
    path('login/', finance_views.login_view, name='login'),
    path('logout/', finance_views.logout_view, name='logout'),
    path('dashboard/', finance_views.customer_dashboard, name='customer_dashboard'),
]
