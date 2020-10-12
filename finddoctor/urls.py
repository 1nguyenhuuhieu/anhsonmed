from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from . import views




urlpatterns = [
    path('', views.index, name='home'),
    path('test/', views.test, name='test'),
    path('doctor/<int:doctor_id>', views.doctor ,name='doctor'),
    path('search/<str:keyword>', views.search, name='search'),
    path('login/',views.loginfinddoctor, name='login'),
    path('register/',views.register, name='register'),
    path('bookappointmenthome/',views.bookappointmenthome, name='bookappointmenthome'),
    path('bookappointment/<int:doctor_id>/',views.bookappointment, name='bookappointment'),


     
]



if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)