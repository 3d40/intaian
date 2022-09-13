import datetime
from django.contrib.auth.tokens import default_token_generator
from django.utils import timezone
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import *
from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.shortcuts import get_list_or_404, render, get_object_or_404, redirect, HttpResponseRedirect, reverse
from .models import *
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from .token import AccountActivationTokenGenerator
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.utils.encoding import force_str as force_text
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth import get_user_model

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .token import account_activation_token
from django.core.mail import EmailMessage
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


def signup(request):
    if request.method == 'GET':
        return render(request, 'registration/register.html')
    if request.method == 'POST':
        form = SignupForm(request.POST)
        # print(form.errors.as_data())
        if form.is_valid():
            pegawai = TPegawaiSapk.objects.filter(nip_baru=request.POST.get('username')).exists()
            if pegawai == True:
                print('data ada')
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                current_site = get_current_site(request)
                mail_subject = 'Aktifkan akun Anda!'
                message = render_to_string('registration/account_activation_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': default_token_generator.make_token(user),
                })
                to_email = form.cleaned_data.get('email')
                email = EmailMessage(mail_subject, message, to=[to_email])
                email.send()
                return HttpResponse('Silahkan komfirmasi email Anda untuk menyelesaikan proses pendaftaran!')
            else:
                return HttpResponse('Data Anda tidak terhubung dengan data kepegawaian Pemerintah Provinsi Jambi!')
    else:
        form = SignupForm()
    return render(request, 'registration/register.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('Terimkasih untuk konfirmasi emailnya. Anda sekarang bisa melakukan login!.')
    else:
        return HttpResponse('link aktifasi email anda sudah kadaluarsa!')

def account_activation_sent(request):
    return render(request, 'registration/account_activation_sent.html')

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

def RiwayatJabatanView(request, nip_baru):
    pegawai = TPegawaiSapk.objects.get(nip_baru=nip_baru)
    jabatan = get_list_or_404(TRiwayatJabatan, nip =nip_baru)
    template_name = 'pegawai/trwjabatan_list.html'
    # form = FormTRiwayatJabatan(instance=pegawai)
    context = {
        'jabatan':jabatan,
        'pegawai':pegawai,
        # 'form':form
    }
    print(pegawai)
    return render(request,template_name, context)

class ListTPegawaisapkjft(ListView):
    model = TPegawaiSapk
    paginate_by = 100  # if pagination is desired
    context_object_name = 'data'
    queryset = TPegawaiSapk.objects.filter(jenis_jabatan = 2)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class ListTPegawaisapkjfu(ListView):
    model = TPegawaiSapk
    paginate_by = 100  # if pagination is desired
    context_object_name = 'data'
    queryset = TPegawaiSapk.objects.filter(jenis_jabatan = 4)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class ListTPegawaisapkjfs(ListView):
    model = TPegawaiSapk
    paginate_by = 100 # if pagination is desired
    context_object_name = 'data'
    queryset = TPegawaiSapk.objects.filter(jenis_jabatan = 1)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

def RiwayatGolonganView(request, nip_baru):
    pegawai = TPegawaiSapk.objects.get(nip_baru=nip_baru)
    golongan = TRiwayatGolongan.objects.filter(id_orang=pegawai.pns_id)
    template_name = 'pegawai/trwgolongan_list.html'
    form = FormTRiwayatGolongan()
    context = {
         'golongan':golongan,
         'pegawai':pegawai,
         'form':form
    }
    return render(request,template_name, context)

def Riwayatdp3View(request, nip_baru):
    pegawai = TPegawaiSapk.objects.get(nip_baru=nip_baru)
    dp3 = TRiwayatDp3.objects.filter(id_pns=pegawai.pns_id)
    template_name = 'pegawai/trwdp3_list.html'
    context = {
         'dp3':dp3,
         'pegawai':pegawai,
    }
    return render(request,template_name, context)

