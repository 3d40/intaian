import datetime

from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
import time, calendar
from .models import TPegawaiSapk
from .filter import FilterTPegawaiSapk
from .forms import *
from django.contrib.auth.models import User
# Create your views here.

@login_required
def home(request):
    data = TPegawaiSapk.objects.all()
    jumlah = data.count()
    pria = data.filter(jenis_kelamin = 'M').count()
    perempuan = data.filter(jenis_kelamin = 'F').count()
    jfs =data.filter(jenis_jabatan = 1).count()
    jft = data.filter(jenis_jabatan= 2).count()
    jfu = data.filter(jenis_jabatan= 4).count()

    senjfs = (jfs/jumlah)*100
    senjft = (jft/jumlah)*100
    senjfu = (jfu/jumlah)*100
    #Golongan I
    ia = data.filter(gol_id=11).count()
    ib = data.filter(gol_id=12).count()
    ic = data.filter(gol_id=13).count()
    id = data.filter(gol_id=14).count()
    totgoli = ia+ib+ic+id
    seni = (totgoli / jumlah) * 100

    # Golongan II
    iia = data.filter(gol_id=21).count()
    iib = data.filter(gol_id=22).count()
    iic = data.filter(gol_id=23).count()
    iid = data.filter(gol_id=24).count()
    totgolii = iia + iib + iic + iid
    senii=(totgolii/jumlah)*100
    print(totgolii, senii)

    # Golongan III
    iiia = data.filter(gol_id=31).count()
    iiib = data.filter(gol_id=32).count()
    iiic = data.filter(gol_id=33).count()
    iiid = data.filter(gol_id=34).count()
    totgoliii = iiia + iiib + iiic + iiid
    seniii = (totgoliii / jumlah) * 100
    print(totgoliii)

    # Golongan III
    iva = data.filter(gol_id=41).count()
    ivb = data.filter(gol_id=42).count()
    ivc = data.filter(gol_id=43).count()
    ivd = data.filter(gol_id=44).count()
    ive = data.filter(gol_id=45).count()
    totgoliv = iva + ivb + ivc + ivd + ive
    seniv = (totgoliv / jumlah) * 100
    print(totgoliv)
    localtime = datetime.datetime.now()

    filterku = FilterTPegawaiSapk(request.GET, queryset=data)
    data = filterku.qs
    formfilter = FormTPegawaiSapk
    context = {
        'data': data, 'jft':jft, 'jfs':jfs,'jfu':jfu,
        'pria': pria,
        'perempuan': perempuan,
        'jumlah': jumlah,
        'i':totgoli,'ii':totgolii,'iii':totgoliii,'iv':totgoliv,'seni':seni,'senii':senii,'seniii':seniii,'seniv':seniv,
        'localtime':localtime,
        'senjft':senjft, 'senjfu':senjfu, 'senjfs':senjfs
    }
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