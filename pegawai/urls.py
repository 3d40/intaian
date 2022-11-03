from django.contrib.auth import views as auth_views
from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
 
app_name = 'pegawai'
urlpatterns = [
    path('', views.LoginView, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.signup, name='signup'),
    path('pegawai/', views.home, name='dashboard'),
    path('pegawai/datalist', views.ListTPegawaisapk.as_view(), name='datalist'),
    path('pegawai/jft', views.ListTPegawaisapkjft.as_view(), name='jft'),
    path('pegawai/jfs', views.ListTPegawaisapkjfs.as_view(), name='jfs'),
    path('pegawai/jfu', views.ListTPegawaisapkjfu.as_view(), name='jfu'),
    path('pegawai/cari', views.CariView, name='cari'),
    path('pegawai/profile/<str:nip_baru>', views.ProfileView, name='profile'),
    path('pegawai/profile/jabatan/<str:nip_baru>', views.RiwayatJabatanView, name='jabatan'),
    path('pegawai/profile/golongan/<str:nip_baru>', views.RiwayatGolonganView, name='golongan'),
    path('pegawai/profile/dp3/<str:nip_baru>', views.Riwayatdp3View, name='dp3'),
    path('pegawai/profile/(<uidb64>[0-9A-Za-z_\-]+)/(<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',views.activate, name='activate'),
    path('pegawai/search', views.search, name='search'),
    path('pegawai/filter', views.filter, name='filter'),
    path('pegawai/pensiun', views.PensiunView, name='pensiun'),

    #input data
    path('pegawai/input/skp', views.InputSkpView.as_view(), name='inputskp'),
    path('pegawai/input/skp/detail/<str:id>', views.SkpDetailView, name='skpdetail'),
    path('pegawai/input/jabatan/tambah', views.InputJabatanView, name='inputjabatan'),
    path('pegawai/input/jabatan/<str:id>', views.EditJabatanView, name='editjabatan'),
    # path('pegawai/input/jabatan/<str:nip>/tambah/', views.TambahJabatanView, name='tambahjabatan'),
    path('pegawai/input/pangkat/<str:id>', views.InputPangkatView, name='inputpangkat'),
] 
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)