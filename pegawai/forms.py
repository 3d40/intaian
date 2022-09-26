from cProfile import label
from tkinter import Widget
from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.models import inlineformset_factory, BaseInlineFormSet

class FormTpegawaiSapk(ModelForm):
    class Meta:
        model = TPegawaiSapk
        fields = ['nip_baru','nama', 'gelar_depan', 'gelar_blk', 'gol', 'tmt_golongan', 'tgl_lhr', 'jenis_kelamin','nik', 'nomor_hp', 'email', 'alamat', 'jenis_pegawai', 'jabatan','unor', 'unor_induk']

class FormTRiwayatJabatan(ModelForm):
    class Meta:
        model = TRiwayatJabatan
        fields = [  'id_jabatan','jenis_jabatan', 'eselon', 'tmt_jabatan', 'nomor_sk', 'tanggal_sk', 'id_satuan_kerja', 'tmt_pelantikan']

class FormTRiwayatGolongan(ModelForm):
    class Meta:
        model = TRiwayatGolongan
        fields = '__all__'

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class OpdForm(ModelForm):
    class Meta:
        model = TPegawaiSapk
        fields = ['unor_induk_bkd']