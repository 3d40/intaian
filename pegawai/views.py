from ast import Slice
from cgitb import enable
import email
from multiprocessing import context
from operator import ge
from pickle import FALSE
from pickletools import int4
from re import template
from dateutil.relativedelta import *
from codecs import namereplace_errors
import datetime
from itertools import count
from pyexpat import model
from tkinter import Y
from turtle import update
from django.conf import settings
from webbrowser import get
from django.contrib.auth.tokens import default_token_generator
from django.utils import timezone
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

from .forms import *
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.views.generic.edit import FormMixin, SingleObjectMixin
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
from .filter import *
from datetime import date
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import os
from django.urls import reverse,reverse_lazy
# Create your views here.
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

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
    localtime = datetime.now()
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
    paginate_by = 25  # if pagination is desired
    context_object_name = 'page_obj'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['form'] = FilterTPegawaiSapk
        return context
    

def signup(request):
    if request.method == 'GET':
        return render(request, 'registration/register.html')
    if request.method == 'POST':
        form = SignupForm(request.POST)
        form1 = OpdForm(request.POST)
        # print(form.errors.as_data())
        if form.is_valid():
            pegawai = TPegawaiSapk.objects.filter(nip_baru=request.POST.get('username')).exists()
            if pegawai == True:
                y = get_object_or_404(TOpd, id = request.POST.get('unor_induk_bkd'))
                x = TPegawaiSapk.objects.get(nip_baru = request.POST.get('username'))
                x.unor_induk_bkd = y
                x.save()
                # if x.unor_induk != y:
                #     print('Data Beda')
                # else:
                #     print('Data Sama')
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
        form1 = OpdForm()
    return render(request, 'registration/register.html', {'form': form, 'form1':form1})


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        opd = get_object_or_404(TPegawaiSapk, nip_baru = user.username)
        TUser.objects.update_or_create(
            pengguna = user,
            user_akses=opd.unor_induk_bkd)
        user.is_active = True
        user.save()
        namadir =str(user.username)
        if not os.path.exists('upload/'+namadir):
            os.makedirs('upload/'+namadir)
        return HttpResponse('Terimkasih untuk konfirmasi emailnya. Anda sekarang bisa melakukan login!.')
    else:
        return HttpResponse('link aktifasi email anda sudah kadaluarsa!')

def account_activation_sent(request):
    return render(request, 'registration/account_activation_sent.html')

def CariView(request):
    if 'q' in request.GET:
        q = request.GET['q']
        multiple_q = Q(
            Q(nama__icontains=q) | 
            Q(nip_baru__icontains=q) | 
            Q(jabatan__nama_jabatan__icontains=q))
        data = TPegawaiSapk.objects.filter(multiple_q)
        jumlah = data.count()
    else:
        data = TPegawaiSapk.objects.all()
    context = {
        'page_obj': data,
        'jumlah':jumlah,
    }
    return render(request, 'pegawai/tpegawaisapk_list.html', context)


def ProfileView(request, nip_baru):
    pegawai = TPegawaiSapk.objects.get(nip_baru=nip_baru)
    template_name = 'pegawai/profilebaru.html'
    form = FormTpegawaiSapk(instance=pegawai)
    print (pegawai)
    context = {
        'pegawai':pegawai,
        'form':form
    }
    return render(request,template_name, context)

def RiwayatJabatanView(request, nip_baru):
    pegawai = get_object_or_404(TPegawaiSapk, nip_baru=nip_baru)
    jabatan = TRiwayatJabatan.objects.filter(nip=nip_baru).order_by('tmt_jabatan')
    template_name = 'pegawai/trwjabatan_list.html'
    context = {
         'jabatan':jabatan,
         'pegawai':pegawai,
         'judul':'Riwayat Jabatan'
    }
    return render(request,template_name, context)


class ListTPegawaisapkjft(ListView):
    model = TPegawaiSapk
    paginate_by = 100  # if pagination is desired
    context_object_name = 'page_obj'
    queryset = TPegawaiSapk.objects.filter(jenis_jabatan = 2)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class ListTPegawaisapkjfu(ListView):
    model = TPegawaiSapk
    paginate_by = 100  # if pagination is desired
    context_object_name = 'page_obj'
    queryset = TPegawaiSapk.objects.filter(jenis_jabatan = 4)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class ListTPegawaisapkjfs(ListView):
    model = TPegawaiSapk
    paginate_by = 100 # if pagination is desired
    context_object_name = 'page_obj'
    queryset = TPegawaiSapk.objects.filter(jenis_jabatan = 1)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

def RiwayatGolonganView(request, nip_baru):
    pegawai = TPegawaiSapk.objects.get(nip_baru=nip_baru)
    golongan = TRiwayatGolongan.objects.filter(id_orang=pegawai.pns_id).order_by('sk_tanggal')
    template_name = 'pegawai/trwgolongan_list.html'
    form = FormTRiwayatGolongan()
    context = {
         'golongan':golongan,
         'pegawai':pegawai,
         'form':form,
         'judul':'Riwayat Golongan'
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


def search(request):
    object_list = TPegawaiSapk.objects.all()
    page_num = request.GET.get('page', 1)
    paginator = Paginator(object_list, 20) # 6 employees per page

    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)
    # user_list = TPegawaiSapk.objects.all()
    # user_filter = FilterTPegawaiSapk(request.GET, queryset=user_list)
    # paginator = Paginator(user_list, 50)
    # page_number = request.GET.get('page', 1)
    # page_obj = paginator.get_page(page_number)
    jumlah = object_list.count()
    return render(request, 'pegawai/pegawai_list.html', {'page_obj':page_obj, 'jumlah':jumlah})

    
def LoginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            request.session['user'] = username
            xxx = TUser.objects.get(pengguna = user)
            print(xxx.user_akses)
            tipeuser = TJenisUser.objects.get(jenis=xxx.jenis)
            print(tipeuser)

            if user.is_active and tipeuser.jenis =='Pegawai':
                pegawai = get_object_or_404(TPegawaiSapk, nip_baru = user)
                login(request,user)
                # return HttpResponseRedirect(reverse('pegawai:dashboard'))
                return render(request, 'pegawai/profilebaru.html',{'pegawai':pegawai})
            elif user.is_active and tipeuser.jenis =='Operator':
                data = get_list_or_404(TPegawaiSapk, unor_induk_bkd = xxx.user_akses)
                login(request,user)
                page_num = request.GET.get('page', 1)
                paginator = Paginator(data, 20)
                try:
                    page_obj = paginator.page(page_num)
                except PageNotAnInteger:
                    page_obj = paginator.page(1)
                except EmptyPage:
                    page_obj = paginator.page(paginator.num_pages)

                return render(request, 'pegawai/pegawai_list.html',{'page_obj':page_obj})
            elif user.is_active and tipeuser.jenis =='Verifikator':
                data = TPegawaiSapk.objects.all()
                login(request,user)
                page_num = request.GET.get('page', 1)
                paginator = Paginator(data, 20)
                try:
                    page_obj = paginator.page(page_num)
                except PageNotAnInteger:
                    page_obj = paginator.page(1)
                except EmptyPage:
                    page_obj = paginator.page(paginator.num_pages)
                return render(request, 'pegawai/pegawai_list.html',{'page_obj':page_obj})
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Akun anda belum terdaftar")
    else:
        return render(request, 'registration/login.html', {})

def filter(request):
    user_list = TPegawaiSapk.objects.all()
    user_filter = FilterTPegawaiSapk(request.GET, queryset=user_list)
    jumlah = user_list.count

    return render(request, 'pegawai/search_results.html', {'filter': user_filter, 'jumlah':jumlah})


def PensiunView(request):
    pegawai = TPegawaiSapk.objects.all()
    for x in pegawai:
        tahun = x.nip_baru[0:4]
        bulan = x.nip_baru[4:6]
        tanggal = x.nip_baru[6:8]
        tgllahir = '%s-%s-%s' %(tanggal,bulan,tahun)
        get_bup = TJabatan.objects.filter(id=x.jabatan)


        # # tgllahir = datetime.strptime(x.tgl_lhr, '%d-%m-%Y')
        # tahun=relativedelta(years=tahun + get_bup.bup)
        # umur = relativedelta(tgllahir, datetime.datetime.now())
        # bulan = str(tgllahir.month)
        # tgl = str(tgllahir.day)
        # tglpensiun = '%s-%s-%s' %(tgl,bulan,str(tahun.years))
        # print(get_bup.bup, tglpensiun) 
        # buat = TPensiun.objects.create(pns_id = x.pns_id, umur = umur.years, tmt_pensiun = inputdbnya)
    return render(request, 'pegawai/pensiun_list.html') 

class InputSkpView(CreateView):
    def get(self, request, *args, **kwargs):
        context = {'form': FormRiwayatSkp()}
        return render(request, 'pegawai/inputskp.html', context)

    def post(self, request, *args, **kwargs):
        form = FormRiwayatSkp(request.POST)
        if form.is_valid():
            book = form.save()
            book.save()
            return HttpResponseRedirect(reverse_lazy('pegawai:skpdetail', args=[book.id]))
        return render(request, 'pegawai/inputskp.html', {'form': form})

def InputJabatanView(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = FormTRiwayatJabatan(request.POST or None)
    if form.is_valid():
        form.save()
    context['form']= form
    return render(request, "pegawai/jabataninput.html", context)

def EditJabatanView(request, id):
    data = TRiwayatJabatan.objects.get(id=id)
    form = FormTRiwayatJabatan(instance=data)
    context={
        'form':form
    }
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('pegawai:jabatan')
    else:
      pass
    return render(request, 'pegawai/jabataninput.html', context)

# class JabatanDetailView(DetailView):
#     model = TRiwayatJabatan
#     context_object_name: 'data'
    
#     def get_object(self, queryset=None):
#         return TRiwayatJabatan.objects.get(id = id)


def SkpDetailView(request, id):
    data = TRiwayatDp3.objects.get(id=id)
    context = {
        'form' : FormRiwayatSkp(instance=data)
    }
   

    return render(request, 'pegawai/triwayatdp3_detail.html', context)

def InputPangkatView(request, id):
    data = TRiwayatGolongan.objects.get(pk=id)
    form = FormTRiwayatGolongan(instance=data)
    form.fields['jenis_kp'].disabled = True
    form.fields['id_golongan'].disabled = True
    form.fields['sk_nomor'].disabled = True
    form.fields['sk_tanggal'].disabled = True
    form.fields['tmt_golongan'].disabled = True
    form.fields['mk_golongan_tahun'].disabled = True
    form.fields['mk_golongan_bulan'].disabled = True
    context={
        'form':form
    }
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('golongan',data.id_orang.nip_baru)
    else:
      pass
    return render(request, 'pegawai/pangkatinput.html', context)

# class InpunPangkatView(UpdateView):
#     model = TRiwayatGolongan
#     form_class = FormTRiwayatGolongan
#     template_name = "pegawai/pangkatinput.html"

#     def get_form(self, form_class=None):
#         form = super(FormTRiwayatGolongan, self).get_form(form_class)
#         if not self.request.user.is_superuser:
#             # Disable these fields
#             form.fields["jenis_kp"].disabled = True
#             form.fields["id_golongan"].disabled = True
#             form.fields["sk_nomor"].disabled = True
#             form.fields["sk_tanggal"].disabled = True
#             form.fields["tmt_golongan"].disabled = True
#             form.fields["mk_golongan_tahun"].disabled = True
#             form.fields["mk_golongan_bulan"].disabled = True
#         return form

#     def form_valid(self, form):
#         form.save()
#         return redirect(reverse("pegawai:golongan"))  


#  register_form = RegistrationForm()
#     if request.method=='POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             new_user = User.objects.create_user(username=request.POST['username'], 
#                                             email=request.POST['email'], 
#                                             password=request.POST['password1'])
#             new_user.is_active = False
#             new_user.save()
#             return HttpResponseRedirect(reverse('index'))
#     return render_to_response('registration/registration_form.html'{'form':register_form})