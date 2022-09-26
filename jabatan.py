# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class TEselon(models.Model):
    id = models.IntegerField(primary_key=True)
    nama = models.CharField(max_length=10)
    max_pangkat = models.IntegerField()
    min_pangkat = models.IntegerField()
    keterangan = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_eselon'


class TJabatan(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    nama_jabatan = models.CharField(db_column='nama_Jabatan', max_length=139)  # Field name made lowercase.
    id_jenis_jabatan = models.IntegerField(db_column='id_Jenis_Jabatan')  # Field name made lowercase.
    jenis_jabatan = models.CharField(max_length=27)
    id_eselon = models.IntegerField()
    bup = models.IntegerField()
    stastus = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 't_jabatan'


class TJenisJabatan(models.Model):
    jenis_jabatan_id = models.CharField(db_column='JENIS_JABATAN_ID', primary_key=True, max_length=1)  # Field name made lowercase.
    jenis_jabatan_nama = models.CharField(db_column='JENIS_JABATAN_NAMA', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_jenis_jabatan'


class TJenisPegawai(models.Model):
    jenis_pegawai_id = models.CharField(db_column='JENIS_PEGAWAI_ID', primary_key=True, max_length=2)  # Field name made lowercase.
    jenis_pegawai_nama = models.CharField(db_column='JENIS_PEGAWAI_NAMA', max_length=60)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_jenis_pegawai'


class TJenisUnor(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=34)  # Field name made lowercase.
    nama = models.CharField(db_column='NAMA', max_length=50)  # Field name made lowercase.
    jenis = models.CharField(db_column='JENIS', max_length=3)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_jenis_unor'


class TJenjangJabatan(models.Model):
    kel_jabatan_id = models.CharField(db_column='KEL_JABATAN_ID', max_length=34)  # Field name made lowercase.
    nama = models.CharField(db_column='NAMA', max_length=115)  # Field name made lowercase.
    id = models.CharField(db_column='ID', unique=True, max_length=34)  # Field name made lowercase.
    min_gol = models.CharField(db_column='MIN_GOL', max_length=3)  # Field name made lowercase.
    max_gol = models.CharField(db_column='MAX_GOL', max_length=3)  # Field name made lowercase.
    tunjangan = models.CharField(db_column='TUNJANGAN', max_length=10)  # Field name made lowercase.
    bup = models.CharField(db_column='BUP', max_length=3)  # Field name made lowercase.
    cepat_kode = models.CharField(db_column='CEPAT_KODE', max_length=6)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_jenjang_jabatan'


class TKelompokJabatan(models.Model):
    rumpun_id = models.CharField(db_column='RUMPUN_ID', max_length=34)  # Field name made lowercase.
    nama = models.CharField(db_column='NAMA', max_length=115)  # Field name made lowercase.
    id = models.CharField(db_column='ID', unique=True, max_length=34)  # Field name made lowercase.
    tugas_pokok = models.CharField(db_column='TUGAS_POKOK', max_length=300)  # Field name made lowercase.
    pejabat_pak = models.CharField(db_column='PEJABAT_PAK', max_length=300)  # Field name made lowercase.
    lingkup = models.CharField(db_column='LINGKUP', max_length=2)  # Field name made lowercase.
    pembina_id = models.CharField(db_column='PEMBINA_ID', max_length=34)  # Field name made lowercase.
    jenis_jabatan_umum_id = models.CharField(db_column='JENIS_JABATAN_UMUM_ID', max_length=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_kelompok_jabatan'


class TKodeAgama(models.Model):
    agama_id = models.CharField(db_column='AGAMA_ID', primary_key=True, max_length=1)  # Field name made lowercase.
    agama_nama = models.CharField(db_column='AGAMA_NAMA', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_kode_agama'


class TKodeGolongan(models.Model):
    kode_golongan = models.CharField(primary_key=True, max_length=2)
    nama_golongan = models.CharField(max_length=5)
    nama_pangkat = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 't_kode_golongan'


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


class TOpd(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=32)  # Field name made lowercase.
    nama_unor = models.CharField(db_column='NAMA_UNOR', max_length=255)  # Field name made lowercase.
    eselon_id = models.CharField(db_column='ESELON_ID', max_length=3)  # Field name made lowercase.
    cepat_kode = models.CharField(db_column='CEPAT_KODE', max_length=15)  # Field name made lowercase.
    nama_jabatan = models.CharField(db_column='NAMA_JABATAN', max_length=255)  # Field name made lowercase.
    nama_pejabat = models.CharField(db_column='NAMA_PEJABAT', max_length=55)  # Field name made lowercase.
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


class TPegawaiSapk(models.Model):
    pns_id = models.CharField(db_column='PNS_ID', primary_key=True, max_length=32)  # Field name made lowercase.
    nip_baru = models.CharField(db_column='NIP_BARU', max_length=18)  # Field name made lowercase.
    nip_lama = models.CharField(db_column='NIP_LAMA', max_length=9, blank=True, null=True)  # Field name made lowercase.
    nama = models.CharField(db_column='NAMA', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gelar_depan = models.CharField(db_column='GELAR_DEPAN', max_length=5, blank=True, null=True)  # Field name made lowercase.
    gelar_blk = models.CharField(db_column='GELAR_BLK', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tempat_lahir_id = models.CharField(db_column='TEMPAT_LAHIR_ID', max_length=32)  # Field name made lowercase.
    tgl_lahir = models.CharField(db_column='TGL_LAHIR', max_length=10, blank=True, null=True)  # Field name made lowercase.
    jenis_kelamin = models.CharField(db_column='JENIS_KELAMIN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    agama_id = models.CharField(db_column='AGAMA_ID', max_length=1)  # Field name made lowercase.
    jenis_kawin_id = models.CharField(db_column='JENIS_KAWIN_ID', max_length=1, blank=True, null=True)  # Field name made lowercase.
    nik = models.CharField(db_column='NIK', max_length=30, blank=True, null=True)  # Field name made lowercase.
    nomor_hp = models.CharField(db_column='NOMOR_HP', max_length=40, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    email_gov = models.CharField(db_column='EMAIL_GOV', max_length=50)  # Field name made lowercase.
    alamat = models.CharField(db_column='ALAMAT', max_length=150, blank=True, null=True)  # Field name made lowercase.
    npwp_nomor = models.CharField(db_column='NPWP_NOMOR', max_length=30, blank=True, null=True)  # Field name made lowercase.
    bpjs = models.CharField(db_column='BPJS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    jenis_pegawai_id = models.CharField(db_column='JENIS_PEGAWAI_ID', max_length=2)  # Field name made lowercase.
    kedudukan_hukum_id = models.CharField(db_column='KEDUDUKAN_HUKUM_ID', max_length=2)  # Field name made lowercase.
    status_cpns_pns = models.CharField(db_column='STATUS_CPNS_PNS', max_length=1)  # Field name made lowercase.
    kartu_pegawai = models.CharField(db_column='KARTU_PEGAWAI', max_length=30, blank=True, null=True)  # Field name made lowercase.
    nomor_sk_cpns = models.CharField(db_column='NOMOR_SK_CPNS', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tgl_sk_cpns = models.CharField(db_column='TGL_SK_CPNS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tmt_cpns = models.CharField(db_column='TMT_CPNS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    nomor_sk_pns = models.CharField(db_column='NOMOR_SK_PNS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tgl_sk_pns = models.CharField(db_column='TGL_SK_PNS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tmt_pns = models.CharField(db_column='TMT_PNS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    gol_awal_id = models.CharField(db_column='GOL_AWAL_ID', max_length=2)  # Field name made lowercase.
    gol_id = models.CharField(db_column='GOL_ID', max_length=2)  # Field name made lowercase.
    tmt_golongan = models.CharField(db_column='TMT_GOLONGAN', max_length=10)  # Field name made lowercase.
    mk_tahun = models.IntegerField(db_column='MK_TAHUN', blank=True, null=True)  # Field name made lowercase.
    mk_bulan = models.IntegerField(db_column='MK_BULAN', blank=True, null=True)  # Field name made lowercase.
    jenis_jabatan_id = models.CharField(db_column='JENIS_JABATAN_ID', max_length=1)  # Field name made lowercase.
    jabatan_id = models.CharField(db_column='JABATAN_ID', max_length=32)  # Field name made lowercase.
    tmt_jabatan = models.CharField(db_column='TMT_JABATAN', max_length=10)  # Field name made lowercase.
    tingkat_pendidikan_id = models.CharField(db_column='TINGKAT_PENDIDIKAN_ID', max_length=2)  # Field name made lowercase.
    pendidikan_id = models.CharField(db_column='PENDIDIKAN_ID', max_length=32)  # Field name made lowercase.
    tahun_lulus = models.CharField(db_column='TAHUN_LULUS', max_length=5)  # Field name made lowercase.
    kpkn_id = models.CharField(db_column='KPKN_ID', max_length=32)  # Field name made lowercase.
    lokasi_kerja_id = models.CharField(db_column='LOKASI_KERJA_ID', max_length=32)  # Field name made lowercase.
    unor_id = models.CharField(db_column='UNOR_ID', max_length=32)  # Field name made lowercase.
    unor_induk_id = models.CharField(db_column='UNOR_INDUK_ID', max_length=32)  # Field name made lowercase.
    instansi_induk_nama = models.CharField(db_column='INSTANSI_INDUK_NAMA', max_length=32)  # Field name made lowercase.
    instansi_kerja_nama = models.CharField(db_column='INSTANSI_KERJA_NAMA', max_length=32)  # Field name made lowercase.
    satuan_kerja_induk_nama = models.CharField(db_column='SATUAN_KERJA_INDUK_NAMA', max_length=32)  # Field name made lowercase.
    satuan_kerja_kerja_nama = models.CharField(db_column='SATUAN_KERJA_KERJA_NAMA', max_length=32)  # Field name made lowercase.
    fhoto = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 't_pegawai_sapk'


class TPendidikan(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=34)  # Field name made lowercase.
    tingkat_pendidikan_id = models.CharField(db_column='TINGKAT_PENDIDIKAN_ID', max_length=3)  # Field name made lowercase.
    nama = models.CharField(db_column='NAMA', max_length=150)  # Field name made lowercase.
    cepat_kode = models.CharField(db_column='CEPAT_KODE', max_length=6)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_pendidikan'


class TRiwayatDp3(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=32)  # Field name made lowercase.
    id_pns = models.CharField(db_column='ID_PNS', max_length=32)  # Field name made lowercase.
    nip_pns = models.CharField(db_column='NIP_PNS', max_length=18)  # Field name made lowercase.
    nama_pns = models.CharField(db_column='NAMA_PNS', max_length=40)  # Field name made lowercase.
    id_jenis_jabatan = models.IntegerField(db_column='ID_JENIS_JABATAN', blank=True, null=True)  # Field name made lowercase.
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
    id_pejabat_penilai = models.CharField(db_column='ID_PEJABAT_PENILAI', max_length=30, blank=True, null=True)  # Field name made lowercase.
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
    nama_unor_atasan_penilai = models.CharField(db_column='NAMA_UNOR_ATASAN_PENILAI', max_length=85, blank=True, null=True)  # Field name made lowercase.
    dokumen = models.CharField(db_column='DOKUMEN', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_riwayat_dp3'


class TRiwayatGolongan(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=32)  # Field name made lowercase.
    id_orang = models.CharField(db_column='Id_Orang', max_length=32)  # Field name made lowercase.
    nip = models.CharField(db_column='NIP', max_length=18)  # Field name made lowercase.
    nama = models.CharField(db_column='Nama', max_length=40)  # Field name made lowercase.
    kode_jenis_kp = models.IntegerField(db_column='Kode_Jenis_KP', blank=True, null=True)  # Field name made lowercase.
    jenis_kp = models.CharField(db_column='Jenis_KP', max_length=52, blank=True, null=True)  # Field name made lowercase.
    id_golongan = models.IntegerField(db_column='Id_Golongan')  # Field name made lowercase.
    golongan = models.CharField(db_column='Golongan', max_length=5)  # Field name made lowercase.
    pangkat = models.CharField(db_column='Pangkat', max_length=23)  # Field name made lowercase.
    sk_nomor = models.CharField(db_column='SK_Nomor', max_length=45, blank=True, null=True)  # Field name made lowercase.
    sk_tanggal = models.CharField(db_column='Sk_Tanggal', max_length=14, blank=True, null=True)  # Field name made lowercase.
    nomor_bkn = models.CharField(db_column='Nomor_BKN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    tanggal_bkn = models.CharField(db_column='Tanggal_BKN', max_length=14, blank=True, null=True)  # Field name made lowercase.
    tmt_golongan = models.CharField(db_column='TMT_Golongan', max_length=14, blank=True, null=True)  # Field name made lowercase.
    jumlah_angka_kredit_utama = models.DecimalField(db_column='Jumlah_Angka_Kredit_Utama', max_digits=8, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    jumlah_angka_kredit_tambahan = models.DecimalField(db_column='Jumlah_Angka_Kredit_Tambahan', max_digits=7, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    mk_golongan_tahun = models.IntegerField(db_column='MK_Golongan_Tahun', blank=True, null=True)  # Field name made lowercase.
    mk_golongan_bulan = models.IntegerField(db_column='MK_Golongan_Bulan', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_riwayat_golongan'


class TRiwayatJabatan(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=32)  # Field name made lowercase.
    id_orang = models.CharField(db_column='Id_Orang', max_length=32)  # Field name made lowercase.
    nip = models.CharField(db_column='NIP', max_length=18)  # Field name made lowercase.
    nama = models.CharField(db_column='Nama', max_length=40)  # Field name made lowercase.
    id_unor = models.CharField(db_column='Id_Unor', max_length=32, blank=True, null=True)  # Field name made lowercase.
    unor = models.CharField(db_column='Unor', max_length=150, blank=True, null=True)  # Field name made lowercase.
    id_jenis_jabatan = models.IntegerField(db_column='Id_Jenis_Jabatan', blank=True, null=True)  # Field name made lowercase.
    jenis_jabatan = models.CharField(db_column='Jenis_Jabatan', max_length=27, blank=True, null=True)  # Field name made lowercase.
    id_jabatan = models.CharField(db_column='Id_Jabatan', max_length=32, blank=True, null=True)  # Field name made lowercase.
    nama_jabatan = models.CharField(db_column='Nama_Jabatan', max_length=139, blank=True, null=True)  # Field name made lowercase.
    id_eselon = models.IntegerField(db_column='Id_Eselon', blank=True, null=True)  # Field name made lowercase.
    eselon = models.CharField(db_column='Eselon', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tmt_jabatan = models.CharField(db_column='TMT_Jabatan', max_length=14)  # Field name made lowercase.
    nomor_sk = models.CharField(db_column='Nomor_SK', max_length=52, blank=True, null=True)  # Field name made lowercase.
    tanggal_sk = models.CharField(db_column='Tanggal_SK', max_length=14, blank=True, null=True)  # Field name made lowercase.
    id_satuan_kerja = models.CharField(db_column='Id_Satuan_Kerja', max_length=32)  # Field name made lowercase.
    tmt_pelantikan = models.CharField(db_column='TMT_Pelantikan', max_length=14, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_riwayat_jabatan'


class TRumpunJabatan(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=34)  # Field name made lowercase.
    nama = models.CharField(db_column='NAMA', max_length=150)  # Field name made lowercase.
    deskripsi = models.CharField(db_column='DESKRIPSI', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_rumpun_jabatan'


class TStatusKawin(models.Model):
    jenis_kawin_id = models.CharField(db_column='JENIS_KAWIN_ID', primary_key=True, max_length=1)  # Field name made lowercase.
    jenis_kawin_nama = models.CharField(db_column='JENIS_KAWIN_NAMA', max_length=15)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_status_kawin'


class TStatusKedudukan(models.Model):
    id_status_kedudukan = models.CharField(db_column='ID_STATUS_KEDUDUKAN', primary_key=True, max_length=2)  # Field name made lowercase.
    nama_status_kedudukan = models.CharField(db_column='NAMA_STATUS_KEDUDUKAN', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_status_kedudukan'


class TTingkatPendidikan(models.Model):
    kode = models.CharField(db_column='KODE', primary_key=True, max_length=3)  # Field name made lowercase.
    nama = models.CharField(db_column='NAMA', max_length=25)  # Field name made lowercase.
    golongan_awal = models.CharField(db_column='GOLONGAN_AWAL', max_length=3)  # Field name made lowercase.
    golongan_akhir = models.CharField(db_column='GOLONGAN_AKHIR', max_length=3)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_tingkat_pendidikan'


class TUnor(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=32)  # Field name made lowercase.
    nama_unor = models.CharField(db_column='NAMA_UNOR', max_length=255)  # Field name made lowercase.
    eselon_id = models.CharField(db_column='ESELON_ID', max_length=3)  # Field name made lowercase.
    cepat_kode = models.CharField(db_column='CEPAT_KODE', max_length=15)  # Field name made lowercase.
    nama_jabatan = models.CharField(db_column='NAMA_JABATAN', max_length=255)  # Field name made lowercase.
    nama_pejabat = models.CharField(db_column='NAMA_PEJABAT', max_length=55)  # Field name made lowercase.
    diatasan_id = models.CharField(db_column='DIATASAN_ID', max_length=32)  # Field name made lowercase.
    instansi_id = models.CharField(db_column='INSTANSI_ID', max_length=32)  # Field name made lowercase.
    pemimpin_non_pns_id = models.CharField(db_column='PEMIMPIN_NON_PNS_ID', max_length=55)  # Field name made lowercase.
    pemimpin_pns_id = models.CharField(db_column='PEMIMPIN_PNS_ID', max_length=32)  # Field name made lowercase.
    jenis_unor_id = models.CharField(db_column='JENIS_UNOR_ID', max_length=32)  # Field name made lowercase.
    unor_induk_id = models.CharField(db_column='UNOR_INDUK_ID', max_length=32)  # Field name made lowercase.
    jumlah_ideal_staff = models.CharField(db_column='JUMLAH_IDEAL_STAFF', max_length=3)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_unor'


class TUser(models.Model):
    user_id = models.CharField(primary_key=True, max_length=40)
    user_pass = models.CharField(max_length=20)
    user_type = models.CharField(max_length=1)
    user_akses = models.CharField(max_length=50)
    pns_id = models.CharField(db_column='PNS_ID', max_length=32)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_user'
