import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class FilterTPegawaiSapk(django_filters.FilterSet):
	nama = CharFilter(field_name='note', lookup_expr='icontains')


	class Meta:
		model = TPegawaiSapk
		fields = '__all__'
		exclude = ['jenis_kelamin', 'date_created']

class PegawaiFilter(django_filters.FilterSet):
    class Meta:
        model = TPegawaiSapk
        fields = '__all__'
