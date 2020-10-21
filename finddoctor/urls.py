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
    path('appointment/',views.appointment, name='appointment'),
    path('appointment/<int:bookappointment_id>',views.appointmentdetail, name='appointmentdetail'),

    #User Profile 
    path('profile/',views.profile, name='profile'),
    path('mycomment/',views.mycomment, name='mycomment'),
    path('alldoctors/',views.alldoctors, name='alldoctors'),
    path('department/<int:department_id>',views.department, name='department'),
    #Ask Doctor
    path('ask/<int:ask_id>',views.ask, name='ask'),

    #404 page
    path('404/', views.page404, name = 'page404'),

    #All Departments
    path('alldepartments/', views.alldepartments, name = 'alldepartments'),


    #All Asks
    path('allasks/', views.allasks, name = 'allasks'),


     
]



if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)