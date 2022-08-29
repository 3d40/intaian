from django.contrib.auth import views as auth_views
from . import views
from django.urls import path
 
app_name = 'pegawai'
urlpatterns = [
    path('', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('pegawai/', views.home, name='dashboard'),
    path('datalist/', views.ListTPegawaisapk.as_view(), name='datalist'),
    path('pegawai/cari', views.CariView, name='cari'),
    path('pegawai/profile/<str:nip_baru>', views.ProfileView, name='profile'),


]