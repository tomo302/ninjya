from django.shortcuts import render, redirect
#19
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
#22
from django.contrib.auth import login, logout
# Create your views here.

def signup_view(request):
    if request.method == 'POST':  
        form = UserCreationForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('articles:list')
    else:
        form = UserCreationForm()  
    return render(request, 'accounts/signup.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        #print(form)
        if form.is_valid():      #21
            # log in the user
            user = form.get_user()
            login(request,user)

            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
        
                return redirect('articles:list') # TOP PAGE
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form':form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('articles:list')