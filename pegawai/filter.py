import django_filters
from django_filters import DateFilter, CharFilter
from django.db.models import Q
from .models import *

class FilterTPegawaiSapk(django_filters.FilterSet):
	nama = CharFilter(field_name='note', lookup_expr='icontains')
	class Meta:
		model = TPegawaiSapk
		fields = ['nip_baru','nama','jenis_jabatan','gelar_depan', 'gelar_blk', 'gol', 'tmt_golongan', 'tgl_lhr', 'jenis_kelamin','nik', 'nomor_hp', 'email', 'alamat', 'jenis_pegawai', 'jabatan','unor', 'unor_induk']

# class PegawaiFilter(django_filters.FilterSet):
# 	q = django_filters.CharFilter(method='filterq',label="Search")
	
# 	class Meta:
# 		model = TPegawaiSapk
# 		fields = ['q']
	
# 	def filterq(self, queryset, name, value):
# 		return queryset.fil(
# 			Q(nama__icontains=value) | Q(nip=value) | jenis_jabatan=value) | Q(gol=value)