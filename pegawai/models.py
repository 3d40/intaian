# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from asyncio.windows_events import NULL
from datetime import datetime
from email.policy import default
import imp
from pyexpat import model
from statistics import mode
from tabnanny import verbose
from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class TJenisJabatan(models.Model):
    jenis_jabatan_id = models.CharField(db_column='JENIS_JABATAN_ID', primary_key=True, max_length=1)  # Field name made lowercase.
    jenis_jabatan_nama = models.CharField(db_column='JENIS_JABATAN_NAMA', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_jenis_jabatan'

    def __str__(self):
        return self.jenis_jabatan_nama


class TJenisPegawai(models.Model):
    jenis_pegawai_id = models.CharField(db_column='JENIS_PEGAWAI_ID', primary_key=True, max_length=2)  # Field name made lowercase.
    jenis_pegawai_nama = models.CharField(db_column='JENIS_PEGAWAI_NAMA', max_length=60)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_jenis_pegawai'

    def __str__(self):
        return self.jenis_pegawai_nama


class TJenisUnor(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=34)  # Field name made lowercase.
    nama = models.CharField(db_column='NAMA', max_length=50)  # Field name made lowercase.
    jenis = models.CharField(db_column='JENIS', max_length=3)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_jenis_unor'

    def __str__(self):
        return self.nama


class TJenjangJabatan(models.Model):
    kel_jabatan= models.ForeignKey('TKelompokJabatan', max_length=34, on_delete=models.DO_NOTHING)  # Field name made lowercase.
    nama = models.CharField(db_column='NAMA', max_length=115)  # Field name made lowercase.
    id = models.CharField(db_column='ID', unique=True, max_length=34, primary_key=True)  # Field name made lowercase.
    min_gol = models.CharField(db_column='MIN_GOL', max_length=3)  # Field name made lowercase.
    max_gol = models.CharField(db_column='MAX_GOL', max_length=3)  # Field name made lowercase.
    tunjangan = models.CharField(db_column='TUNJANGAN', max_length=10)  # Field name made lowercase.
    bup = models.CharField(db_column='BUP', max_length=3)  # Field name made lowercase.
    cepat_kode = models.CharField(db_column='CEPAT_KODE', max_length=6)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_jenjang_jabatan'

    def __str__(self):
        return self.nama


class TKelompokJabatan(models.Model):
    id = models.CharField(db_column='ID', unique=True, max_length=34, primary_key=True)  # Field name made lowercase.
    nama = models.CharField(db_column='NAMA', max_length=115)  # Field name made lowercase.
    rumpun= models.ForeignKey('TRumpunJabatan', max_length=34, on_delete=models.CASCADE)  # Field name made lowercase.
    tugas_pokok = models.CharField(db_column='TUGAS_POKOK', max_length=300)  # Field name made lowercase.
    pejabat_pak = models.CharField(db_column='PEJABAT_PAK', max_length=300)  # Field name made lowercase.
    lingkup = models.CharField(db_column='LINGKUP', max_length=2)  # Field name made lowercase.
    pembina= models.ForeignKey('TUnor', max_length=34, on_delete=models.DO_NOTHING)  # Field name made lowercase.
    jenis_jabatan_umum= models.ForeignKey('TJenisJabatan', max_length=2, on_delete=models.DO_NOTHING)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_kelompok_jabatan'

    def __str__(self):
        return self.nama


class TKodeAgama(models.Model):
    agama_id = models.CharField(db_column='AGAMA_ID', primary_key=True, max_length=1)  # Field name made lowercase.
    agama_nama = models.CharField(db_column='AGAMA_NAMA', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_kode_agama'

    def __str__(self):
        return self.agama_nama


class TKodeGolongan(models.Model):
    id = models.CharField(primary_key=True, max_length=2)
    nama_golongan = models.CharField(max_length=5)
    nama_pangkat = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 't_kode_golongan'

    def __str__(self):
        return self.nama_golongan


class TLokasi(models.Model):
    lokasi_id = models.CharField(db_column='LOKASI_ID', primary_key=True, max_length=32)  # Field name made lowercase.
    kanreg_id = models.CharField(db_column='KANREG_ID', max_length=2)  # Field name made lowercase.
    nama = models.CharField(db_column='NAMA', max_length=50)  # Field name made lowercase.
    cepat_kode = models.CharField(db_column='CEPAT_KODE', max_length=10)  # Field name made lowercase.
    jenis = models.CharField(db_column='JENIS', max_length=3)  # Field name made lowercase.
    jenis_kabupaten = models.CharField(db_column='JENIS_KABUPATEN', max_length=25)  # Field name made lowercase.
    jenis_desa = models.CharField(db_column='JENIS_DESA', max_length=15)  # Field name made lowercase.
    ibukota = models.CharField(db_column='IBUKOTA', max_length=25)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_lokasi'

    def __str__(self):
        return self.nama


class TPegawaiSapk(models.Model):
    pns_id = models.CharField(db_column='PNS_ID', primary_key=True, max_length=32)  # Field name made lowercase.
    nip_baru = models.CharField(db_column='NIP_BARU', max_length=18)  # Field name made lowercase.
    nip_lama = models.CharField(db_column='NIP_LAMA', max_length=9, blank=True, null=True)  # Field name made lowercase.
    nama = models.CharField(db_column='NAMA', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gelar_depan = models.CharField(db_column='GELAR_DEPAN', max_length=5, blank=True, null=True)  # Field name made lowercase.
    gelar_blk = models.CharField(db_column='GELAR_BLK', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tempat_lahir= models.ForeignKey('TLokasi', max_length=32, on_delete=models.CASCADE, related_name='TEMPAT_LAHIR', null = True, blank = True)  # Field name made lowercase.
    tgl_lhr = models.CharField(db_column='TGL_LAHIR', max_length=10, blank=True, null=True)  # Field name made lowercase.
    jenis_kelamin = models.CharField(db_column='JENIS_KELAMIN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    agama= models.ForeignKey('TKodeAgama', max_length=1, on_delete=models.DO_NOTHING, blank=True, null=True)  # Field name made lowercase.
    jenis_kawin = models.ForeignKey('TStatusKawin', max_length=1, blank=True, null=True, on_delete=models.DO_NOTHING)  # Field name made lowercase.
    nik = models.CharField(db_column='NIK', max_length=30, blank=True, null=True)  # Field name made lowercase.
    nomor_hp = models.CharField(db_column='NOMOR_HP', max_length=40, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=50, blank=True, null=True)
    alamat = models.CharField(db_column='ALAMAT', max_length=150, blank=True, null=True)  # Field name made lowercase.
    npwp_nomor = models.CharField(db_column='NPWP_NOMOR', max_length=30, blank=True, null=True)  # Field name made lowercase.
    bpjs = models.CharField(db_column='BPJS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    jenis_pegawai = models.ForeignKey('TJenisPegawai', max_length=2, on_delete=models.DO_NOTHING, blank=True, null=True)  # Field name made lowercase.
    kedudukan_hukum = models.ForeignKey('TStatusKedudukan', max_length=2, on_delete=models.DO_NOTHING, blank=True, null=True)  # Field name made lowercase.
    status_cpns_pns = models.CharField(db_column='STATUS_CPNS_PNS', max_length=1)  # Field name made lowercase.
    kartu_pegawai = models.CharField(db_column='KARTU_PEGAWAI', max_length=30, blank=True, null=True)  # Field name made lowercase.
    nomor_sk_cpns = models.CharField(db_column='NOMOR_SK_CPNS', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tgl_sk_cpns = models.CharField(db_column='TGL_SK_CPNS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tmt_cpns = models.CharField(db_column='TMT_CPNS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    nomor_sk_pns = models.CharField(db_column='NOMOR_SK_PNS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tgl_sk_pns = models.CharField(db_column='TGL_SK_PNS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tmt_pns = models.CharField(db_column='TMT_PNS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    gol_awal = models.ForeignKey('TKodeGolongan', max_length=2, on_delete=models.DO_NOTHING, blank=True, null=True)  # Field name made lowercase.
    gol= models.ForeignKey('TKodeGolongan',related_name='GOL_ID', max_length=2, on_delete=models.DO_NOTHING, blank=True, null=True)  # Field name made lowercase.
    tmt_golongan = models.CharField(db_column='TMT_GOLONGAN', max_length=10)  # Field name made lowercase.
    mk_tahun = models.IntegerField(db_column='MK_TAHUN', blank=True, null=True)  # Field name made lowercase.
    mk_bulan = models.IntegerField(db_column='MK_BULAN', blank=True, null=True)  # Field name made lowercase.
    jenis_jabatan= models.ForeignKey('TJenisJabatan',on_delete=models.DO_NOTHING, blank=True, null=True)  # Field name made lowercase.
    jabatan = models.ForeignKey('TJabatan', on_delete=models.DO_NOTHING, null=True, db_column='JABATAN_ID')  # Field name made lowercase.
    tingkat_pendidikan= models.ForeignKey('TTingkatPendidikan', on_delete=models.DO_NOTHING, blank=True, null=True)  # Field name made lowercase.
    pendidikan= models.ForeignKey('TPendidikan', max_length=32, on_delete=models.DO_NOTHING, blank=True, null=True)  # Field name made lowercase.
    kpkn= models.CharField(db_column='KPKN_ID', max_length=32)  # Field name made lowercase.
    lokasi_kerja = models.ForeignKey('TLokasi',related_name='LOKASI_KERJA_ID', on_delete=models.DO_NOTHING, blank=True, null=True)  # Field name made lowercase.
    unor= models.ForeignKey('TUnor', max_length=32, on_delete=models.CASCADE, related_name='UNOR_ID')  # Field name made lowercase.
    unor_induk = models.ForeignKey('TOpd', on_delete=models.DO_NOTHING, related_name='UNOR_INDUK_ID', null=True, blank=True)  # Field name made lowercase.
    unor_induk_bkd = models.ForeignKey('TOpd', on_delete=models.DO_NOTHING, db_column='UNOR_INDUK_BKD', verbose_name='Instansi', null=True, blank=True)  # Field name made lowercase.
    instansi_induk_nama = models.CharField(db_column='INSTANSI_INDUK_NAMA', max_length=150, blank=True, null=True)  # Field name made lowercase.
    instansi_kerja_nama= models.CharField(db_column='INSTANSI_KERJA_NAMA', max_length=150, blank=True, null=True)  # Field name made lowercase.
    satuan_kerja_induk_nama = models.CharField(db_column='SATUAN_KERJA_INDUK_NAMA', max_length=150, blank=True, null=True)  # Field name made lowercase.
    satuan_kerja_kerja_nama= models.CharField(db_column='SATUAN_KERJA_KERJA_NAMA', max_length=150, blank=True, null=True)  
    tmt_pensiun = models.DateField(db_column='TMT_PENSIUN', blank=True, null=True)# Field name made lowercase.
    fhoto=models.ImageField(upload_to='media', height_field=None, width_field=None, max_length=100)

    class Meta:
        managed = False
        db_table = 't_pegawai_sapk'
        

    def __str__(self):
        return self.nama


class TPendidikan(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=34)  # Field name made lowercase.
    tingkat_pendidikan = models.ForeignKey('TPendidikan', max_length=3, on_delete=models.DO_NOTHING)  # Field name made lowercase.
    nama = models.CharField(db_column='NAMA', max_length=150)  # Field name made lowercase.
    cepat_kode = models.CharField(db_column='CEPAT_KODE', max_length=6)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_pendidikan'

    def __str__(self):
        return self.nama


class TRumpunJabatan(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=34)  # Field name made lowercase.
    nama = models.CharField(db_column='NAMA', max_length=150)  # Field name made lowercase.
    deskripsi = models.CharField(db_column='DESKRIPSI', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_rumpun_jabatan'

    def __str__(self):
        return self.nama


class TStatusKawin(models.Model):
    jenis_kawin_id = models.CharField(db_column='JENIS_KAWIN_ID', primary_key=True, max_length=1)  # Field name made lowercase.
    jenis_kawin_nama = models.CharField(db_column='JENIS_KAWIN_NAMA', max_length=15)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_status_kawin'

    def __str__(self):
        return self.jenis_kawin_nama


class TStatusKedudukan(models.Model):
    id_status_kedudukan = models.CharField(db_column='ID_STATUS_KEDUDUKAN', primary_key=True, max_length=2)  # Field name made lowercase.
    nama_status_kedudukan = models.CharField(db_column='NAMA_STATUS_KEDUDUKAN', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_status_kedudukan'

    def __str__(self):
        return self.nama_status_kedudukan


class TTingkatPendidikan(models.Model):
    kode = models.CharField(db_column='KODE', primary_key=True, max_length=3)  # Field name made lowercase.
    nama = models.CharField(db_column='NAMA', max_length=25)  # Field name made lowercase.
    golongan_awal = models.CharField(db_column='GOLONGAN_AWAL', max_length=3)  # Field name made lowercase.
    golongan_akhir = models.CharField(db_column='GOLONGAN_AKHIR', max_length=3)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_tingkat_pendidikan'

    def __str__(self):
        return self.nama


class TUnor(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=32)  # Field name made lowercase.
    instansi_id = models.CharField(db_column='INSTANSI_ID', max_length=32)  # Field name made lowercase.
    diatasan_id = models.CharField(db_column='DIATASAN_ID', max_length=32)  # Field name made lowercase.
    eselon_id = models.CharField(db_column='ESELON_ID', max_length=3)  # Field name made lowercase.
    nama_unor = models.CharField(db_column='NAMA_UNOR', max_length=250)  # Field name made lowercase.
    nama_jabatan = models.CharField(db_column='NAMA_JABATAN', max_length=250, blank=True, null=True)  # Field name made lowercase.
    # unor_order = models.IntegerField(db_column='UNOR_ORDER', blank=True, null=True)  # Field name made lowercase.
    # status = models.CharField(db_column='STATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    pemimpin_pns= models.ForeignKey('TPegawaiSapk', max_length=32, blank=True, null=True, on_delete=models.DO_NOTHING)  # Field name made lowercase.
    cepat_kode = models.CharField(db_column='CEPAT_KODE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    jenis_unor_id = models.CharField(db_column='JENIS_UNOR_ID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    nama_pejabat = models.CharField(db_column='NAMA_PEJABAT', max_length=70, blank=True, null=True)  # Field name made lowercase.
    unor_induk = models.CharField(db_column='UNOR_INDUK_ID', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_unor'

    def __str__(self):
        return self.nama_unor


class TUser(models.Model):
    pengguna=models.ForeignKey(User, db_column='pengguna',on_delete=models.CASCADE, related_name="usernames") 
    jenis = models.ForeignKey('TJenisUser', db_column='jenis', on_delete=models.CASCADE, verbose_name='Jenis Pengguna', default=1)
    user_akses = models.ForeignKey('TOpd', db_column='user_akses', on_delete=models.CASCADE, verbose_name='Nama OPD')
    waktu_login = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        managed = False
        db_table = 't_user'

    def __str__(self):
        return self.pengguna.username


class TRiwayatJabatan(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=32,)  # Field name made lowercase.
    nip = models.CharField(db_column='NIP', max_length=18)  # Field name made lowercase.
    id_orang = models.ForeignKey('TPegawaiSapk', max_length=32, on_delete=models.CASCADE, db_column='Id_Orang')  # Field name made lowercase.
    nama = models.CharField(db_column='Nama', max_length=40)  # Field name made lowercase.
    unor = models.ForeignKey('TUnor', max_length=32, on_delete=models.CASCADE, db_column='Id_Unor')  # Field name made lowercase.
    jenis_jabatan = models.ForeignKey('TJenisJabatan', blank=True, null=True, on_delete=models.CASCADE, db_column='Id_Jenis_Jabatan')  # Field name made lowercase.
    id_jabatan = models.ForeignKey('TJabatan' , max_length=32, on_delete=models.CASCADE, db_column='id_jabatan',  verbose_name ='Nama Jabatan')  # Field name made lowercase.
    id_eselon = models.ForeignKey('TEselon' , max_length=32, on_delete=models.CASCADE, db_column='id_eselon')  # Field name made lowercase.
    eselon = models.CharField(db_column='Eselon', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tmt_jabatan = models.DateField(db_column='TMT_JABATAN', max_length=14, default='01-01-2022')  # Field name made lowercase.
    nomor_sk = models.CharField(db_column='Nomor_SK', max_length=52, blank=True, null=True)  # Field name made lowercase.
    tanggal_sk = models.DateField(db_column='Tanggal_SK', blank=True, null=True)  # Field name made lowercase.
    id_satuan_kerja = models.CharField(db_column='Id_Satuan_Kerja', max_length=32, verbose_name ='Satuan Kerja')  # Field name made lowercase.
    tmt_pelantikan = models.DateField(db_column='TMT_Pelantikan', blank=True, null=True) # Field name made lowercase.
    dokumen = models.FileField(upload_to='documents/')
    # slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for title alias.')

    class Meta:
        managed = False
        db_table = 't_riwayat_jabatan'

    def __str__(self):
        return self.nama

class TRiwayatGolongan(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=32)  # Field name made lowercase.
    id_orang = models.ForeignKey('TPegawaiSapk', max_length=32, on_delete=models.CASCADE, db_column='id_orang')  # Field name made lowercase.
    kode_jenis_kp = models.IntegerField(db_column='Kode_Jenis_KP', blank=True, null=True)  # Field name made lowercase.
    jenis_kp = models.CharField(db_column='Jenis_KP', max_length=52, blank=True, null=True)  # Field name made lowercase.
    id_golongan = models.ForeignKey('TKodeGolongan', max_length=32, on_delete=models.CASCADE, db_column='id_golongan')  # Field name made lowercase.
    sk_nomor = models.CharField(db_column='SK_Nomor', max_length=45, blank=True, null=True)  # Field name made lowercase.
    sk_tanggal = models.DateField(db_column='Sk_Tanggal', max_length=14, blank=True, null=True)  # Field name made lowercase.
    nomor_bkn = models.CharField(db_column='Nomor_BKN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    tanggal_bkn = models.DateField(db_column='Tanggal_BKN', max_length=14, blank=True, null=True)  # Field name made lowercase.
    tmt_golongan = models.CharField(db_column='TMT_Golongan', max_length=14, blank=True, null=True)  # Field name made lowercase.
    jumlah_angka_kredit_utama = models.DecimalField(db_column='Jumlah_Angka_Kredit_Utama', max_digits=8, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    jumlah_angka_kredit_tambahan = models.DecimalField(db_column='Jumlah_Angka_Kredit_Tambahan', max_digits=7, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    mk_golongan_tahun = models.IntegerField(db_column='MK_Golongan_Tahun', blank=True, null=True)  # Field name made lowercase.
    mk_golongan_bulan = models.IntegerField(db_column='MK_Golongan_Bulan', blank=True, null=True)  # Field name made lowercase.
    dokumen = models.FileField(upload_to='documents/')
    
    class Meta:
        managed = False
        db_table = 't_riwayat_golongan'

    def __str__(self):
        return self.jenis_kp

class TRiwayatDp3(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=32)  # Field name made lowercase.
    id_pns = models.ForeignKey('TPegawaiSapk', max_length=32, on_delete=models.CASCADE, db_column='id_pns')
    id_jenis_jabatan = models.ForeignKey('TJenisJabatan', max_length=32, on_delete=models.CASCADE, db_column='id_jenis_jabatan')
    nama_jenis_jabatan = models.CharField(db_column='NAMA_JENIS_JABATAN', max_length=27, blank=True, null=True)  # Field name made lowercase.
    tahun = models.IntegerField(db_column='TAHUN')  # Field name made lowercase.
    kesetiaan = models.DecimalField(db_column='KESETIAAN', max_digits=5, decimal_places=2)  # Field name made lowercase.
    prestasi_kerja = models.DecimalField(db_column='PRESTASI_KERJA', max_digits=5, decimal_places=2)  # Field name made lowercase.
    tanggung_jawab = models.DecimalField(db_column='TANGGUNG_JAWAB', max_digits=5, decimal_places=2)  # Field name made lowercase.
    ketaatan = models.DecimalField(db_column='KETAATAN', max_digits=5, decimal_places=2)  # Field name made lowercase.
    kejujuran = models.DecimalField(db_column='KEJUJURAN', max_digits=5, decimal_places=2)  # Field name made lowercase.
    kerjasama = models.DecimalField(db_column='KERJASAMA', max_digits=5, decimal_places=2)  # Field name made lowercase.
    prakarsa = models.DecimalField(db_column='PRAKARSA', max_digits=5, decimal_places=2)  # Field name made lowercase.
    kepemimpinan = models.IntegerField(db_column='KEPEMIMPINAN')  # Field name made lowercase.
    jumlah = models.DecimalField(db_column='JUMLAH', max_digits=6, decimal_places=2)  # Field name made lowercase.
    nilai_ratarata = models.DecimalField(db_column='NILAI_RATARATA', max_digits=5, decimal_places=2)  # Field name made lowercase.
    status_pejabat_penilai = models.CharField(db_column='STATUS_PEJABAT_PENILAI', max_length=9, blank=True, null=True)  # Field name made lowercase.
    id_pejabat_penilai = models.ForeignKey('TPegawaiSapk', max_length=32, on_delete=models.CASCADE, db_column='id_pejabat_penilai', related_name='id_pejabat_penilai')
    nipnrp_pejabat_penilai = models.CharField(db_column='NIPNRP_PEJABAT_PENILAI', max_length=19, blank=True, null=True)  # Field name made lowercase.
    nama_pejabat_penilai = models.CharField(db_column='NAMA_PEJABAT_PENILAI', max_length=32, blank=True, null=True)  # Field name made lowercase.
    jabatan_pejabat_penilai = models.CharField(db_column='JABATAN_PEJABAT_PENILAI', max_length=95, blank=True, null=True)  # Field name made lowercase.
    golongan_pejabat_penilai = models.CharField(db_column='GOLONGAN_PEJABAT_PENILAI', max_length=6, blank=True, null=True)  # Field name made lowercase.
    tmt_golongan_pejabat_penilai = models.CharField(db_column='TMT_GOLONGAN_PEJABAT_PENILAI', max_length=14, blank=True, null=True)  # Field name made lowercase.
    nama_unor_pejabat_penilai = models.CharField(db_column='NAMA_UNOR_PEJABAT_PENILAI', max_length=94, blank=True, null=True)  # Field name made lowercase.
    status_atasan_penilai = models.CharField(db_column='STATUS_ATASAN_PENILAI', max_length=9, blank=True, null=True)  # Field name made lowercase.
    id_atasan_penilai = models.CharField(db_column='ID_ATASAN_PENILAI', max_length=30, blank=True, null=True)  # Field name made lowercase.
    nipnrp_atasan_penilai = models.CharField(db_column='NIPNRP_ATASAN_PENILAI', max_length=30, blank=True, null=True)  # Field name made lowercase.
    nama_atasan_penilai = models.CharField(db_column='NAMA_ATASAN_PENILAI', max_length=30, blank=True, null=True)  # Field name made lowercase.
    jabatan_atasan_penilai = models.CharField(db_column='JABATAN_ATASAN_PENILAI', max_length=81, blank=True, null=True)  # Field name made lowercase.
    golongan_atasan_penilai = models.CharField(db_column='GOLONGAN_ATASAN_PENILAI', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tmt_golongan_atasan_penilai = models.CharField(db_column='TMT_GOLONGAN_ATASAN_PENILAI', max_length=14, blank=True, null=True)  # Field name made lowercase.
    nama_unor_atasan_penilai = models.CharField(db_column='NAMA_UNOR_ATASAN_PENILAI', max_length=85, blank=True, null=True) # Field name made lowercase.
    dokumen = models.FileField(upload_to='documents/')

    class Meta:
        managed = False
        db_table = 't_riwayat_dp3'

    def __str__(self):
        return str(self.id_pns)




class TOpd(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=32)  # Field name made lowercase.
    nama_unor = models.CharField(db_column='NAMA_UNOR', max_length=255, verbose_name = 'Instansi')  # Field name made lowercase.
    eselon_id = models.CharField(db_column='ESELON_ID', max_length=3)  # Field name made lowercase.
    cepat_kode = models.CharField(db_column='CEPAT_KODE', max_length=15)  # Field name made lowercase.
    nama_jabatan = models.CharField(db_column='NAMA_JABATAN', max_length=255)  # Field name made lowercase.
    nama_pejabat = models.ForeignKey('TPegawaiSapk' ,db_column='NAMA_PEJABAT', on_delete=models.DO_NOTHING)  # Field name made lowercase.
    diatasan_id = models.CharField(db_column='DIATASAN_ID', max_length=32)  # Field name made lowercase.
    instansi_id = models.CharField(db_column='INSTANSI_ID', max_length=32)  # Field name made lowercase.
    pemimpin_non_pns_id = models.CharField(db_column='PEMIMPIN_NON_PNS_ID', max_length=55)  # Field name made lowercase.
    pemimpin_pns_id = models.CharField(db_column='PEMIMPIN_PNS_ID', max_length=32)  # Field name made lowercase.
    jenis_unor_id = models.CharField(db_column='JENIS_UNOR_ID', max_length=32)  # Field name made lowercase.
    unor_induk = models.CharField(db_column='UNOR_INDUK', max_length=32)  # Field name made lowercase.
    jumlah_ideal_staff = models.CharField(db_column='JUMLAH_IDEAL_STAFF', max_length=3)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_opd'
    
    def __str__(self):
        return str(self.nama_unor)

class TJabatan(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    nama_jabatan = models.CharField(db_column='nama_Jabatan', max_length=139)  # Field name made lowercase.
    id_jenis_jabatan = models.ForeignKey('TJenisJabatan', db_column='id_jenis_jabatan', on_delete=models.DO_NOTHING)  # Field name made lowercase.
    jenis_jabatan = models.CharField(max_length=27)
    id_eselon = models.ForeignKey('Teselon', db_column='id_eselon', on_delete=models.DO_NOTHING)
    bup = models.IntegerField()
    stastus = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 't_jabatan'
    
    def __str__(self):
        return str(self.nama_jabatan)

class TEselon(models.Model):
    id = models.IntegerField(primary_key=True)
    nama = models.CharField(max_length=10)
    maxgol = models.ForeignKey('TKodeGolongan', on_delete=models.DO_NOTHING,db_column='max_pangkat', related_name='maxgol')
    mingol = models.ForeignKey('TKodeGolongan', on_delete=models.DO_NOTHING, db_column='min_pangkat', related_name='mingol')
    keterangan = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_eselon'
    
    def __str__(self):
        return str(self.nama)


class TJenisUser(models.Model):
    id=models.IntegerField(primary_key=True, auto_created=True)
    jenis_choice = [
        ('Verifikator', 'Verifikator'),
        ('Operator', 'Operator'),
        ('Pegawai', 'Pegawai'),
        ]
    jenis =models.CharField(max_length=20, default='Pegawai', choices=jenis_choice)
    
    class Meta:
        managed = False
        db_table = 't_jenis_user'

    def __str__(self):
        return str(self.jenis)


class TPensiun(models.Model):
    pns_id= models.ForeignKey('TPegawaiSapk', related_name='orang_id', on_delete=models.DO_NOTHING, blank=True, null=True)
    jabatan=models.ForeignKey('TJabatan', related_name='jabatan_id',  on_delete=models.DO_NOTHING, blank=True, null=True)
    umur = models. IntegerField()
    tmt_pensiun = models.DateField()
    
    class Meta:
        managed = False
        db_table = 't_pensiun'
    
    def __str__(self):
        return str(self.pns_id)


