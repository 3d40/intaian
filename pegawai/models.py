# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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
    rumpun= models.ForeignKey('TRumpunJabatan', max_length=34, on_delete=models.CASCADE)  # Field name made lowercase.
    nama = models.CharField(db_column='NAMA', max_length=115)  # Field name made lowercase.
    id = models.CharField(db_column='ID', unique=True, max_length=34, primary_key=True)  # Field name made lowercase.
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
    kode_golongan = models.CharField(primary_key=True, max_length=2)
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
    lokasi= models.ForeignKey(TLokasi, max_length=32, on_delete=models.CASCADE)  # Field name made lowercase.
    tgl_lhr = models.CharField(db_column='TGL_LHR', max_length=10, blank=True, null=True)  # Field name made lowercase.
    jenis_kelamin = models.CharField(db_column='JENIS_KELAMIN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    agama= models.ForeignKey(TKodeAgama, max_length=1, on_delete=models.CASCADE)  # Field name made lowercase.
    jenis_kawin = models.ForeignKey('TStatusKawin', max_length=1, blank=True, null=True, on_delete=models.DO_NOTHING)  # Field name made lowercase.
    nik = models.CharField(db_column='NIK', max_length=30, blank=True, null=True)  # Field name made lowercase.
    nomor_hp = models.CharField(db_column='NOMOR_HP', max_length=40, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    alamat = models.CharField(db_column='ALAMAT', max_length=150, blank=True, null=True)  # Field name made lowercase.
    npwp_nomor = models.CharField(db_column='NPWP_NOMOR', max_length=30, blank=True, null=True)  # Field name made lowercase.
    bpjs = models.CharField(db_column='BPJS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    jenis_pegawai = models.ForeignKey('TJenisPegawai', max_length=2, on_delete=models.CASCADE)  # Field name made lowercase.
    kedudukan_hukum = models.ForeignKey('TStatusKedudukan', max_length=2, on_delete=models.CASCADE)  # Field name made lowercase.
    status_cpns_pns = models.CharField(db_column='STATUS_CPNS_PNS', max_length=1)  # Field name made lowercase.
    kartu_pegawai = models.CharField(db_column='KARTU_PEGAWAI', max_length=30, blank=True, null=True)  # Field name made lowercase.
    nomor_sk_cpns = models.CharField(db_column='NOMOR_SK_CPNS', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tgl_sk_cpns = models.CharField(db_column='TGL_SK_CPNS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tmt_cpns = models.CharField(db_column='TMT_CPNS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    nomor_sk_pns = models.CharField(db_column='NOMOR_SK_PNS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tgl_sk_pns = models.CharField(db_column='TGL_SK_PNS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tmt_pns = models.CharField(db_column='TMT_PNS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    gol_awal = models.ForeignKey('TKodeGolongan', max_length=2, on_delete=models.CASCADE)  # Field name made lowercase.
    gol= models.ForeignKey('TKodeGolongan',related_name='GOL_ID', max_length=2, on_delete=models.CASCADE)  # Field name made lowercase.
    tmt_golongan = models.CharField(db_column='TMT_GOLONGAN', max_length=10)  # Field name made lowercase.
    mk_tahun = models.IntegerField(db_column='MK_TAHUN', blank=True, null=True)  # Field name made lowercase.
    mk_bulan = models.IntegerField(db_column='MK_BULAN', blank=True, null=True)  # Field name made lowercase.
    jenis_jabatan= models.ForeignKey('TJenisJabatan',on_delete=models.DO_NOTHING)  # Field name made lowercase.
    jabatan_id = models.IntegerField(db_column='JABATAN_ID')  # Field name made lowercase.
    tingkat_pendidikan_id = models.CharField(db_column='TINGKAT_PENDIDIKAN_ID', max_length=2)  # Field name made lowercase.
    pendidikan= models.ForeignKey('TPendidikan', max_length=32, on_delete=models.CASCADE)  # Field name made lowercase.
    kpkn= models.CharField(db_column='KPKN_ID', max_length=32)  # Field name made lowercase.
    lokasi_kerja = models.ForeignKey('TLokasi', max_length=32, related_name='LOKASI_KERJA_ID', on_delete=models.CASCADE)  # Field name made lowercase.
    unor= models.ForeignKey('TUnor', max_length=32, on_delete=models.CASCADE, related_name='UNOR_ID')  # Field name made lowercase.
    unor_induk = models.ForeignKey('TUnor', on_delete=models.CASCADE, related_name='UNOR_INDUK_ID')  # Field name made lowercase.
    instansi_induk = models.ForeignKey('TUnor', max_length=32, on_delete=models.CASCADE, related_name='INSTANSI_INDUK_ID')  # Field name made lowercase.
    instansi_kerja= models.ForeignKey('TUnor', max_length=32, on_delete=models.CASCADE, related_name='INSTANSI_KERJA_ID')  # Field name made lowercase.
    satuan_kerja_induk = models.ForeignKey('TUnor', max_length=32, on_delete=models.CASCADE, related_name='SATUAN_KERJA_INDUK_ID')  # Field name made lowercase.
    satuan_kerja_kerja= models.ForeignKey('TUnor', max_length=32, on_delete=models.CASCADE, related_name='SATUAN_KERJA_KERJA_ID')  # Field name made lowercase.

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
    unor_id = models.CharField(db_column='UNOR_ID', primary_key=True, max_length=32)  # Field name made lowercase.
    instansi_id = models.CharField(db_column='INSTANSI_ID', max_length=32)  # Field name made lowercase.
    diatasan_id = models.CharField(db_column='DIATASAN_ID', max_length=32)  # Field name made lowercase.
    eselon_id = models.CharField(db_column='ESELON_ID', max_length=3)  # Field name made lowercase.
    nama_unor = models.CharField(db_column='NAMA_UNOR', max_length=250)  # Field name made lowercase.
    nama_jabatan = models.CharField(db_column='NAMA_JABATAN', max_length=250, blank=True, null=True)  # Field name made lowercase.
    unor_order = models.IntegerField(db_column='UNOR_ORDER', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    pemimpin_pns= models.ForeignKey('TPegawaiSapk', max_length=32, blank=True, null=True, on_delete=models.DO_NOTHING)  # Field name made lowercase.
    cepat_kode = models.CharField(db_column='CEPAT_KODE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    jenis_unor_id = models.CharField(db_column='JENIS_UNOR_ID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    nama_pejabat = models.CharField(db_column='NAMA_PEJABAT', max_length=70, blank=True, null=True)  # Field name made lowercase.
    induk_unor_id = models.CharField(db_column='INDUK_UNOR_ID', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_unor'

    def __str__(self):
        return self.nama_unor


class TUser(models.Model):
    user_id = models.CharField(primary_key=True, max_length=40)
    user_pass = models.CharField(max_length=20)
    user_type = models.CharField(max_length=1)
    user_akses = models.CharField(max_length=50)
    pns_id = models.CharField(db_column='PNS_ID', max_length=32)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_user'

    def __str__(self):
        return self.nama
