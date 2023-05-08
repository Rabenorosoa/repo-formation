from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from accountsApp.forms import UserForm,ProfileForm


# Create your views here.
def registerV(request):
    if request.user.is_authenticated:
        return redirect('myApp:home')
    
    if request.method == 'POST':
        form = UserForm(request.POST)
        ProfileF =ProfileForm(request.POST)
        if form.is_valid() and ProfileF.is_valid():
            user=form.save(commit=False)
            Profile = ProfileF.save(commit=False)
            Profile.user = user 
            user.save()
            Profile.save()
            return redirect('myApp:home')
    else:
        form =UserForm()
        ProfileF =ProfileForm()
    context={'form': form , 'profile':ProfileF}
    
    return render(request, 'accountsApp/register.html', context)