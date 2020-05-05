"""BudgetAppNew URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from BudgetAPP.views import *
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('Registration/Home', Home.as_view(), name="home"),
    path('Registration/', Registration.as_view(), name="register_user"),
    path('Registration/Login', Login.as_view(), name="login_user"),
    path('Logout/', logout.as_view(), name="logout_user"),
    path('CreateExpense/', CreateExpense.as_view(), name="create_expense"),
    path('ListExpense/', ListExpense.as_view(), name="list_expense"),
    path('Datesum/', CalculateSumDate.as_view(), name="date_sum"),
    path('Categorysum/', CalculateSumCateg.as_view(), name="cat_sum"),



]