from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import TPegawaiSapk
from .filter import FilterTPegawaiSapk
from django.contrib.auth.models import User
# Create your views here.

@login_required
def home(request):
    data = TPegawaiSapk.objects.all()
    jumlah = data.count()
    laki_laki = TPegawaiSapk.objects.filter(jenis_kelamin = 'M').count()
    perempuan = TPegawaiSapk.objects.filter(jenis_kelamin = 'F').count()
    filterku = FilterTPegawaiSapk(request.GET, queryset=data)
    data = filterku.qs
    context = {
        'data': data,
        'laki-laki': laki_laki,
        'perempuan': perempuan,
        'jumlah': jumlah
    }
    print(jumlah, laki_laki, perempuan)
    return render(request, "registration/success.html", context)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})