from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static


from . import views




urlpatterns = [
    path('', views.index, name='home'),
    path('test/', views.test, name='test'),
    path('doctor/<int:doctor_id>', views.doctor ,name='doctor'),
    path('search/<str:keyword>', views.search, name='search'),
    path('login/', views.loginfinddoctor, name='login'),
    re_path(r'login/', views.loginfinddoctor, name='login'),
    path('logout/',views.logoutfinddoctor, name='logout'),
    path('register/',views.register, name='register'),
    path('bookappointmenthome/',views.bookappointmenthome, name='bookappointmenthome'),
    path('bookappointmenthome/success/', views.bookappointmentsuccess, name='bookappointmentsuccess'),
    path('bookappointmentsuccesswithdoctor/<int:doctor_id>', views.bookappointmentsuccesswithdoctor, name='bookappointmentsuccesswithdoctor'),
    
   
    path('bookappointment/<int:doctor_id>/',views.bookappointment, name='bookappointment'),


     
]



if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)