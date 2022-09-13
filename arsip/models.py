from django.db import models
from pegawai.models import TPegawaiSapk, TKodeGolongan
# Create your models here.
class TPangkat (models.Model):
    id_pns = models.ForeignKey(TPegawaiSapk, max_length=32, on_delete=models.CASCADE, db_column='id_pns')
    pangkat = models.ForeignKey(TKodeGolongan,on_delete=models.CASCADE, db_column='pangkat')
    nomor_pertek = models.CharField(max_length=50)
    tgl_pertek = models.DateField()
    nomor_sk =models.CharField(max_length=50)
    tgl_sk = models.DateField()
    mk_bulan = models.IntegerField(null=True)
    mk_tahun = models.IntegerField(null=True)
    tmt_pangkat = models.DateField()
    dokument = models.FileField(upload_to='dokumen/upload/pangkat')

    class Meta:
        managed = False
        db_table = 'T_Pangkat'

        def __str__(self):
            return self.pangkat