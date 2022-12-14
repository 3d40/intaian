# Generated by Django 4.1 on 2022-12-16 04:45

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import pegawai.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TBerkas',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', models.IntegerField(choices=[('1', 'User'), ('2', 'Verifikasi'), ('3', 'Valid'), ('4', 'Rejected')], default=1, verbose_name=(('1', 'User'), ('2', 'Verifikasi'), ('3', 'Valid'), ('4', 'Rejected')))),
            ],
            options={
                'db_table': 't_berkas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TEselon',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=10)),
                ('keterangan', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 't_eselon',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TJabatan',
            fields=[
                ('id', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('nama_jabatan', models.CharField(db_column='nama_Jabatan', max_length=139)),
                ('jenis_jabatan', models.CharField(max_length=27)),
                ('bup', models.IntegerField()),
                ('stastus', models.CharField(max_length=5)),
            ],
            options={
                'db_table': 't_jabatan',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TJenisJabatan',
            fields=[
                ('jenis_jabatan_id', models.CharField(db_column='JENIS_JABATAN_ID', max_length=1, primary_key=True, serialize=False)),
                ('jenis_jabatan_nama', models.CharField(db_column='JENIS_JABATAN_NAMA', max_length=30)),
            ],
            options={
                'db_table': 't_jenis_jabatan',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TJenisPegawai',
            fields=[
                ('jenis_pegawai_id', models.CharField(db_column='JENIS_PEGAWAI_ID', max_length=2, primary_key=True, serialize=False)),
                ('jenis_pegawai_nama', models.CharField(db_column='JENIS_PEGAWAI_NAMA', max_length=60)),
            ],
            options={
                'db_table': 't_jenis_pegawai',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TJenisUnor',
            fields=[
                ('id', models.CharField(db_column='ID', max_length=34, primary_key=True, serialize=False)),
                ('nama', models.CharField(db_column='NAMA', max_length=50)),
                ('jenis', models.CharField(db_column='JENIS', max_length=3)),
            ],
            options={
                'db_table': 't_jenis_unor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TJenisUser',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('jenis', models.CharField(choices=[('Verifikator', 'Verifikator'), ('Operator', 'Operator'), ('Pegawai', 'Pegawai')], default='Pegawai', max_length=20)),
            ],
            options={
                'db_table': 't_jenis_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TJenjangJabatan',
            fields=[
                ('nama', models.CharField(db_column='NAMA', max_length=115)),
                ('id', models.CharField(db_column='ID', max_length=34, primary_key=True, serialize=False, unique=True)),
                ('min_gol', models.CharField(db_column='MIN_GOL', max_length=3)),
                ('max_gol', models.CharField(db_column='MAX_GOL', max_length=3)),
                ('tunjangan', models.CharField(db_column='TUNJANGAN', max_length=10)),
                ('bup', models.CharField(db_column='BUP', max_length=3)),
                ('cepat_kode', models.CharField(db_column='CEPAT_KODE', max_length=6)),
            ],
            options={
                'db_table': 't_jenjang_jabatan',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TKelompokJabatan',
            fields=[
                ('id', models.CharField(db_column='ID', max_length=34, primary_key=True, serialize=False, unique=True)),
                ('nama', models.CharField(db_column='NAMA', max_length=115)),
                ('tugas_pokok', models.CharField(db_column='TUGAS_POKOK', max_length=300)),
                ('pejabat_pak', models.CharField(db_column='PEJABAT_PAK', max_length=300)),
                ('lingkup', models.CharField(db_column='LINGKUP', max_length=2)),
            ],
            options={
                'db_table': 't_kelompok_jabatan',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TKodeAgama',
            fields=[
                ('agama_id', models.CharField(db_column='AGAMA_ID', max_length=1, primary_key=True, serialize=False)),
                ('agama_nama', models.CharField(blank=True, db_column='AGAMA_NAMA', max_length=10, null=True)),
            ],
            options={
                'db_table': 't_kode_agama',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TKodeGolongan',
            fields=[
                ('id', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('nama_golongan', models.CharField(max_length=5)),
                ('nama_pangkat', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 't_kode_golongan',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TLokasi',
            fields=[
                ('lokasi_id', models.CharField(db_column='LOKASI_ID', max_length=32, primary_key=True, serialize=False)),
                ('kanreg_id', models.CharField(db_column='KANREG_ID', max_length=2)),
                ('nama', models.CharField(db_column='NAMA', max_length=50)),
                ('cepat_kode', models.CharField(db_column='CEPAT_KODE', max_length=10)),
                ('jenis', models.CharField(db_column='JENIS', max_length=3)),
                ('jenis_kabupaten', models.CharField(db_column='JENIS_KABUPATEN', max_length=25)),
                ('jenis_desa', models.CharField(db_column='JENIS_DESA', max_length=15)),
                ('ibukota', models.CharField(db_column='IBUKOTA', max_length=25)),
            ],
            options={
                'db_table': 't_lokasi',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TOpd',
            fields=[
                ('id', models.CharField(db_column='ID', max_length=32, primary_key=True, serialize=False)),
                ('nama_unor', models.CharField(db_column='NAMA_UNOR', max_length=255, verbose_name='Instansi')),
                ('eselon_id', models.CharField(db_column='ESELON_ID', max_length=3)),
                ('cepat_kode', models.CharField(db_column='CEPAT_KODE', max_length=15)),
                ('nama_jabatan', models.CharField(db_column='NAMA_JABATAN', max_length=255)),
                ('diatasan_id', models.CharField(db_column='DIATASAN_ID', max_length=32)),
                ('instansi_id', models.CharField(db_column='INSTANSI_ID', max_length=32)),
                ('pemimpin_non_pns_id', models.CharField(db_column='PEMIMPIN_NON_PNS_ID', max_length=55)),
                ('pemimpin_pns_id', models.CharField(db_column='PEMIMPIN_PNS_ID', max_length=32)),
                ('jenis_unor_id', models.CharField(db_column='JENIS_UNOR_ID', max_length=32)),
                ('unor_induk', models.CharField(db_column='UNOR_INDUK', max_length=32)),
                ('jumlah_ideal_staff', models.CharField(db_column='JUMLAH_IDEAL_STAFF', max_length=3)),
            ],
            options={
                'db_table': 't_opd',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TPegawaiSapk',
            fields=[
                ('pns_id', models.CharField(db_column='PNS_ID', max_length=32, primary_key=True, serialize=False)),
                ('nip_baru', models.CharField(db_column='NIP_BARU', max_length=18)),
                ('nip_lama', models.CharField(blank=True, db_column='NIP_LAMA', max_length=9, null=True)),
                ('nama', models.CharField(blank=True, db_column='NAMA', max_length=50, null=True)),
                ('gelar_depan', models.CharField(blank=True, db_column='GELAR_DEPAN', max_length=5, null=True)),
                ('gelar_blk', models.CharField(blank=True, db_column='GELAR_BLK', max_length=20, null=True)),
                ('tgl_lhr', models.DateField(blank=True, db_column='TGL_LAHIR', max_length=10, null=True)),
                ('jenis_kelamin', models.CharField(blank=True, db_column='JENIS_KELAMIN', max_length=1, null=True)),
                ('nik', models.CharField(blank=True, db_column='NIK', max_length=30, null=True)),
                ('nomor_hp', models.CharField(blank=True, db_column='NOMOR_HP', max_length=40, null=True)),
                ('email', models.CharField(blank=True, db_column='EMAIL', max_length=50, null=True)),
                ('alamat', models.CharField(blank=True, db_column='ALAMAT', max_length=150, null=True)),
                ('npwp_nomor', models.CharField(blank=True, db_column='NPWP_NOMOR', max_length=30, null=True)),
                ('bpjs', models.CharField(blank=True, db_column='BPJS', max_length=50, null=True)),
                ('status_cpns_pns', models.CharField(db_column='STATUS_CPNS_PNS', max_length=1)),
                ('kartu_pegawai', models.CharField(blank=True, db_column='KARTU_PEGAWAI', max_length=30, null=True)),
                ('nomor_sk_cpns', models.CharField(blank=True, db_column='NOMOR_SK_CPNS', max_length=40, null=True)),
                ('tgl_sk_cpns', models.DateField(blank=True, db_column='TGL_SK_CPNS', max_length=10, null=True)),
                ('tmt_cpns', models.DateField(blank=True, db_column='TMT_CPNS', max_length=10, null=True)),
                ('nomor_sk_pns', models.CharField(blank=True, db_column='NOMOR_SK_PNS', max_length=50, null=True)),
                ('tgl_sk_pns', models.DateField(blank=True, db_column='TGL_SK_PNS', max_length=10, null=True)),
                ('tmt_pns', models.DateField(blank=True, db_column='TMT_PNS', max_length=10, null=True)),
                ('tmt_golongan', models.CharField(db_column='TMT_GOLONGAN', max_length=10)),
                ('mk_tahun', models.IntegerField(blank=True, db_column='MK_TAHUN', null=True)),
                ('mk_bulan', models.IntegerField(blank=True, db_column='MK_BULAN', null=True)),
                ('kpkn', models.CharField(db_column='KPKN_ID', max_length=32)),
                ('instansi_induk_nama', models.CharField(blank=True, db_column='INSTANSI_INDUK_NAMA', max_length=150, null=True)),
                ('instansi_kerja_nama', models.CharField(blank=True, db_column='INSTANSI_KERJA_NAMA', max_length=150, null=True)),
                ('satuan_kerja_induk_nama', models.CharField(blank=True, db_column='SATUAN_KERJA_INDUK_NAMA', max_length=150, null=True)),
                ('satuan_kerja_kerja_nama', models.CharField(blank=True, db_column='SATUAN_KERJA_KERJA_NAMA', max_length=150, null=True)),
                ('tmt_pensiun', models.DateField(blank=True, db_column='TMT_PENSIUN', null=True)),
                ('fhoto', models.ImageField(upload_to='media')),
            ],
            options={
                'db_table': 't_pegawai_sapk',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TPendidikan',
            fields=[
                ('id', models.CharField(db_column='ID', max_length=34, primary_key=True, serialize=False)),
                ('nama', models.CharField(db_column='NAMA', max_length=150)),
                ('cepat_kode', models.CharField(db_column='CEPAT_KODE', max_length=6)),
            ],
            options={
                'db_table': 't_pendidikan',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TRiwayatDp3',
            fields=[
                ('id', models.UUIDField(db_column='ID', default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('tahun', models.IntegerField(db_column='TAHUN', default='2010')),
                ('kesetiaan', models.DecimalField(db_column='KESETIAAN', decimal_places=2, max_digits=5)),
                ('prestasi_kerja', models.DecimalField(db_column='PRESTASI_KERJA', decimal_places=2, max_digits=5)),
                ('tanggung_jawab', models.DecimalField(db_column='TANGGUNG_JAWAB', decimal_places=2, max_digits=5)),
                ('ketaatan', models.DecimalField(db_column='KETAATAN', decimal_places=2, max_digits=5)),
                ('kejujuran', models.DecimalField(db_column='KEJUJURAN', decimal_places=2, max_digits=5)),
                ('kerjasama', models.DecimalField(db_column='KERJASAMA', decimal_places=2, max_digits=5)),
                ('prakarsa', models.DecimalField(db_column='PRAKARSA', decimal_places=2, max_digits=5)),
                ('kepemimpinan', models.IntegerField(db_column='KEPEMIMPINAN')),
                ('jumlah', models.DecimalField(db_column='JUMLAH', decimal_places=2, max_digits=6)),
                ('nilai_ratarata', models.DecimalField(db_column='NILAI_RATARATA', decimal_places=2, max_digits=5)),
                ('status_pejabat_penilai', models.CharField(blank=True, db_column='STATUS_PEJABAT_PENILAI', max_length=9, null=True)),
                ('nipnrp_pejabat_penilai', models.CharField(blank=True, db_column='NIPNRP_PEJABAT_PENILAI', max_length=19, null=True)),
                ('nama_pejabat_penilai', models.CharField(blank=True, db_column='NAMA_PEJABAT_PENILAI', max_length=32, null=True)),
                ('jabatan_pejabat_penilai', models.CharField(blank=True, db_column='JABATAN_PEJABAT_PENILAI', max_length=95, null=True)),
                ('golongan_pejabat_penilai', models.CharField(blank=True, db_column='GOLONGAN_PEJABAT_PENILAI', max_length=6, null=True)),
                ('tmt_golongan_pejabat_penilai', models.CharField(blank=True, db_column='TMT_GOLONGAN_PEJABAT_PENILAI', max_length=14, null=True)),
                ('nama_unor_pejabat_penilai', models.CharField(blank=True, db_column='NAMA_UNOR_PEJABAT_PENILAI', max_length=94, null=True)),
                ('status_atasan_penilai', models.CharField(blank=True, db_column='STATUS_ATASAN_PENILAI', max_length=9, null=True)),
                ('id_atasan_penilai', models.CharField(blank=True, db_column='ID_ATASAN_PENILAI', max_length=30, null=True)),
                ('nipnrp_atasan_penilai', models.CharField(blank=True, db_column='NIPNRP_ATASAN_PENILAI', max_length=30, null=True)),
                ('nama_atasan_penilai', models.CharField(blank=True, db_column='NAMA_ATASAN_PENILAI', max_length=30, null=True)),
                ('jabatan_atasan_penilai', models.CharField(blank=True, db_column='JABATAN_ATASAN_PENILAI', max_length=81, null=True)),
                ('golongan_atasan_penilai', models.CharField(blank=True, db_column='GOLONGAN_ATASAN_PENILAI', max_length=12, null=True)),
                ('tmt_golongan_atasan_penilai', models.CharField(blank=True, db_column='TMT_GOLONGAN_ATASAN_PENILAI', max_length=14, null=True)),
                ('nama_unor_atasan_penilai', models.CharField(blank=True, db_column='NAMA_UNOR_ATASAN_PENILAI', max_length=85, null=True)),
                ('dokumen', models.FileField(upload_to=pegawai.models._upload_path_skp)),
            ],
            options={
                'db_table': 't_riwayat_dp3',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TRiwayatGolongan',
            fields=[
                ('id', models.CharField(db_column='ID', max_length=32, primary_key=True, serialize=False)),
                ('nip_baru', models.CharField(blank=True, db_column='NIP', max_length=18, null=True)),
                ('kode_jenis_kp', models.IntegerField(blank=True, db_column='Kode_Jenis_KP', null=True)),
                ('jenis_kp', models.CharField(blank=True, db_column='Jenis_KP', max_length=52, null=True)),
                ('sk_nomor', models.CharField(blank=True, db_column='SK_Nomor', max_length=45, null=True)),
                ('sk_tanggal', models.DateField(blank=True, db_column='Sk_Tanggal', default='1900-01-01', max_length=14, null=True)),
                ('nomor_bkn', models.CharField(blank=True, db_column='Nomor_BKN', max_length=30, null=True)),
                ('tanggal_bkn', models.DateField(db_column='Tanggal_BKN', default='1900-01-01', max_length=14, null=True)),
                ('tmt_golongan', models.DateField(blank=True, db_column='TMT_Golongan', max_length=14, null=True)),
                ('jumlah_angka_kredit_utama', models.DecimalField(blank=True, db_column='Jumlah_Angka_Kredit_Utama', decimal_places=3, max_digits=8, null=True)),
                ('jumlah_angka_kredit_tambahan', models.DecimalField(blank=True, db_column='Jumlah_Angka_Kredit_Tambahan', decimal_places=3, max_digits=7, null=True)),
                ('mk_golongan_tahun', models.IntegerField(blank=True, db_column='MK_Golongan_Tahun', null=True)),
                ('mk_golongan_bulan', models.IntegerField(blank=True, db_column='MK_Golongan_Bulan', null=True)),
                ('dokumen', models.FileField(null=True, upload_to=pegawai.models._upload_path_kp, validators=[django.core.validators.FileExtensionValidator(['pdf'])])),
                ('nama', models.CharField(blank=True, db_column='Nama', max_length=255, null=True)),
            ],
            options={
                'db_table': 't_riwayat_golongan',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TRumpunJabatan',
            fields=[
                ('id', models.CharField(db_column='ID', max_length=34, primary_key=True, serialize=False)),
                ('nama', models.CharField(db_column='NAMA', max_length=150)),
                ('deskripsi', models.CharField(db_column='DESKRIPSI', max_length=255)),
            ],
            options={
                'db_table': 't_rumpun_jabatan',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TStatusKawin',
            fields=[
                ('jenis_kawin_id', models.CharField(db_column='JENIS_KAWIN_ID', max_length=1, primary_key=True, serialize=False)),
                ('jenis_kawin_nama', models.CharField(db_column='JENIS_KAWIN_NAMA', max_length=15)),
            ],
            options={
                'db_table': 't_status_kawin',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TStatusKedudukan',
            fields=[
                ('id_status_kedudukan', models.CharField(db_column='ID_STATUS_KEDUDUKAN', max_length=2, primary_key=True, serialize=False)),
                ('nama_status_kedudukan', models.CharField(db_column='NAMA_STATUS_KEDUDUKAN', max_length=100)),
            ],
            options={
                'db_table': 't_status_kedudukan',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TTingkatPendidikan',
            fields=[
                ('kode', models.CharField(db_column='KODE', max_length=3, primary_key=True, serialize=False)),
                ('nama', models.CharField(db_column='NAMA', max_length=25)),
                ('golongan_awal', models.CharField(db_column='GOLONGAN_AWAL', max_length=3)),
                ('golongan_akhir', models.CharField(db_column='GOLONGAN_AKHIR', max_length=3)),
            ],
            options={
                'db_table': 't_tingkat_pendidikan',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TUnor',
            fields=[
                ('id', models.CharField(db_column='ID', max_length=32, primary_key=True, serialize=False)),
                ('instansi_id', models.CharField(db_column='INSTANSI_ID', max_length=32)),
                ('diatasan_id', models.CharField(db_column='DIATASAN_ID', max_length=32)),
                ('eselon_id', models.CharField(db_column='ESELON_ID', max_length=3)),
                ('nama_unor', models.CharField(db_column='NAMA_UNOR', max_length=250)),
                ('nama_jabatan', models.CharField(blank=True, db_column='NAMA_JABATAN', max_length=250, null=True)),
                ('cepat_kode', models.CharField(blank=True, db_column='CEPAT_KODE', max_length=10, null=True)),
                ('jenis_unor_id', models.CharField(blank=True, db_column='JENIS_UNOR_ID', max_length=32, null=True)),
                ('nama_pejabat', models.CharField(blank=True, db_column='NAMA_PEJABAT', max_length=70, null=True)),
                ('unor_induk', models.CharField(blank=True, db_column='UNOR_INDUK_ID', max_length=32, null=True)),
            ],
            options={
                'db_table': 't_unor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('waktu_login', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
            options={
                'db_table': 't_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TRiwayatJabatan',
            fields=[
                ('id', models.UUIDField(db_column='ID', default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('tmt_jabatan', models.DateField(blank=True, db_column='TMT_JABATAN', default='1900-01-01', max_length=14, null=True)),
                ('nomor_sk', models.CharField(blank=True, db_column='Nomor_SK', max_length=52, null=True)),
                ('tanggal_sk', models.DateField(blank=True, db_column='Tanggal_SK', default='1900-01-01', null=True)),
                ('tmt_pelantikan', models.DateField(blank=True, db_column='TMT_Pelantikan', default='1900-01-01', null=True)),
                ('dokumen', models.FileField(upload_to=pegawai.models._upload_path_jabatan)),
                ('berkas', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pegawai.tberkas')),
                ('eselon', models.ForeignKey(db_column='id_eselon', default=53, on_delete=django.db.models.deletion.CASCADE, to='pegawai.teselon', verbose_name='Eselon')),
                ('id_jabatan', models.ForeignKey(db_column='id_jabatan', on_delete=django.db.models.deletion.CASCADE, to='pegawai.tjabatan', verbose_name='Nama Jabatan')),
                ('jenis_jabatan', models.ForeignKey(blank=True, db_column='Id_Jenis_Jabatan', null=True, on_delete=django.db.models.deletion.CASCADE, to='pegawai.tjenisjabatan')),
                ('orang', models.ForeignKey(blank=True, db_column='Id_Orang', null=True, on_delete=django.db.models.deletion.CASCADE, to='pegawai.tpegawaisapk')),
                ('unor', models.ForeignKey(db_column='Id_Unor', on_delete=django.db.models.deletion.CASCADE, to='pegawai.tunor')),
            ],
            options={
                'db_table': 't_riwayat_jabatan',
                'managed': True,
            },
        ),
    ]
