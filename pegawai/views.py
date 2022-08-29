import datetime
from django.utils import timezone
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import *
from django.views.generic.list import ListView
from django.db.models import Q
from django.shortcuts import get_list_or_404, render, get_object_or_404, redirect, HttpResponseRedirect, reverse

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
    context = {
        'data': data, 'jft':jft, 'jfs':jfs,'jfu':jfu,
        'pria': pria,
        'perempuan': perempuan,
        'jumlah': jumlah,
        'i':totgoli,'ii':totgolii,'iii':totgoliii,'iv':totgoliv,'seni':seni,'senii':senii,'seniii':seniii,'seniv':seniv,
        'localtime':localtime,
        'senjft':senjft, 'senjfu':senjfu, 'senjfs':senjfs
    }
    return render(request, "pegawai/dashboard.html", context)


class ListTPegawaisapk(ListView):
    model = TPegawaiSapk
    paginate_by = 100  # if pagination is desired
    context_object_name = 'data'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


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

def CariView(request):
    if 'q' in request.GET:
        q = request.GET['q']
        multiple_q = Q(Q(nama__icontains=q) | Q(nip_baru__icontains=q))
        data = TPegawaiSapk.objects.filter(multiple_q)
    else:
        data = TPegawaiSapk.objects.all()
    context = {
        'data': data
    }
    return render(request, 'pegawai/tpegawaisapk_list.html', context)


def ProfileView(request, nip_baru):
    pegawai = TPegawaiSapk.objects.get(nip_baru=nip_baru)
    template_name = 'pegawai/profile.html'
    form = FormTpegawaiSapk(instance=pegawai)
    context = {
        'pegawai':pegawai,
        'form':form
    }
    return render(request,template_name, context)

