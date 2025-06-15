from django.shortcuts import render,redirect

from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # redirect to login page after successful register
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})
# Create your views here.
