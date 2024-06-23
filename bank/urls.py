"""Bank_Website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from bank import views
from django.contrib.auth.views import LogoutView

# urlpatterns=[
#     path("", views.index, name='bank' ),
#      path('create_account', views.create_account, name='create_account'),
#       path('auth_login', views.auth_login, name='auth_login'),
#       path('logout',views.logout,name='logout'),
#       path('main', views.main, name='main'),
#       path('account_summary/', views.account_summary_view, name='account_summary'),
#       path('money_transfer',views.money_transfer, name='money_transfer'),
#       path('loan_application',views.loan_application, name='loan_application'),
#       path('ewallet',views.ewallet,name='ewallet'),
#       path('online_payment',views.online_payment, name='online_payment'),
#       path('account_settings',views.account_settings, name='account_settings'),
#       path('edit_account',views.edit_account, name='edit_account'),
# ]

from django.urls import path
from .views import home_view, account_summary_view, logout_confirm_view, transfer_money_view, transaction_history_view, pay_bills_view, alerts_view, profile_view

urlpatterns = [
     path("", views.index, name='bank' ),
       path("index/", views.index, name='bank' ),
      path('create_account', views.create_account, name='create_account'),
     path('auth_login', views.auth_login, name='auth_login'),
    path('home/', home_view, name='home'),
    path('account_summary/', account_summary_view, name='account_summary'),
    path('transfer_money/', transfer_money_view, name='transfer_money'),
    path('transaction_history/', transaction_history_view, name='transaction_history'),
    path('pay_bills/', pay_bills_view, name='pay_bills'),
    path('alerts/', alerts_view, name='alerts'),
    path('profile/', profile_view, name='profile'),
     path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('logout_confirm/', logout_confirm_view, name='logout_confirm'),
      
]


