
from django.urls import path
from accountsApp import views
from django.contrib.auth import views as Views
from.forms import LoginForm

app_name = 'accountsApp'

urlpatterns = [
    path('register/', views.registerV, name='register'),
    path('login/', Views.LoginView.as_view(template_name='accountsApp/login.html',
        redirect_authenticated_user = True, authentication_form = LoginForm ) , name='login'),
    path('logout/', Views.LogoutView.as_view(template_name='accountsApp/logout.html', 
        next_page ='accountsApp:login') , name='logout'),
    ]