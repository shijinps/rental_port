from django.urls import path
from adminapp import views

urlpatterns = [
    path('', views.index, name='home'),
    path('cont/', views.contact, name='contact'),
    path('user/', views.userinfo, name='signin'),
    path('userview/', views.userview, name='userview'),
    path('book/', views.bookdata, name='booking'),
    path('bookingview/', views.bookingview, name='viewbooking'),
    path('carview/', views.carview, name='carview'),
    path('login/', views.loginview, name='login'),
    path('logout/', views.logout_view, name='logout'),  # ✅ Added trailing slash and name
    path('sign_up/', views.sign_up, name='signup'),
    path('reset/', views.Resethome, name='reset'),
    path('passwordreset/', views.resetPassword, name='passwordreset'),
]
