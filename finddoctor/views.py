import datetime
from django.utils import timezone

from django.shortcuts import render
from django.shortcuts import redirect

from django.shortcuts import HttpResponse

from .models import Doctor,Department,Education, UserProfile, BookApartment, ReviewDoctor, ReviewDoctor, AppointMent
from itertools import chain
from django.contrib.auth import authenticate,login,logout


from django.contrib.auth.models import User

from django.db.models import Avg

import random
# Create your views here.

def index(request):
  

    context = {}
    

    doctors = Doctor.objects.all()
    departments = Department.objects.all()
    doctor_names = []
    for i in doctors:
        if i.name not in doctor_names:
            doctor_names.append(i.name)
    for j in departments:
        doctor_names.append(j.name)

    top_doctors_list = Doctor.objects.all().filter(showinhome=True)
    top_departments_list = Department.objects.all().filter(showinhome=True)
    top_doctors_list_id = []
    for i in top_doctors_list:
        top_doctors_list_id.append(i.id)
    top_doctors_education = Education.objects.all().filter(doctor_id__in=top_doctors_list_id).filter(main=True)
    
    context.update({'top_doctors_list': top_doctors_list,
                'doctor_names':doctor_names,
                'top_doctors_education':  top_doctors_education,
                'page_title': "Home",
                'top_departments_list':  top_departments_list
    })
    return render(request,'index.html', context)


def doctor(request, doctor_id):
    
    doctor = Doctor.objects.get(pk=doctor_id)
    otplist = AppointMent.objects.all().filter(doctor=doctor)
   
    if request.method == 'POST':
        verify = False
        points = request.POST.get('points')
        if points is None:
            points = 3
        comment = request.POST.get('comment')
        user = User.objects.get(pk = request.user.id)
        if otplist:
            for otp in otplist:

                if otp.vertify_code == int(request.POST.get('otp')):

                    verify = True
                    AppointMent.objects.filter(vertify_code=otp.vertify_code).delete()
                    break
       
        newreview = ReviewDoctor(user = user, stars = points, comment=comment, doctor=doctor , verify= verify)
        newreview.save()
    
        return redirect('doctor', doctor_id)

    educations = Education.objects.all().filter(doctor_id = doctor_id)
    comments = ReviewDoctor.objects.all().filter(doctor_id = doctor_id)
    allcomments =  comments.count()
    if allcomments:
        pointavg = ReviewDoctor.objects.all().filter(doctor_id = doctor_id).aggregate(Avg('stars'))
        pointavg = round(pointavg['stars__avg'],1)
    else:
        pointavg = 0
   


   
    
    
    onepoint = comments.filter(stars=1).count()
    twopoint = comments.filter(stars=2).count()
    threepoint = comments.filter(stars=3).count()
    fourpoint = comments.filter(stars=4).count()
    fivepoint = comments.filter(stars=5).count()

  
    context = { 'doctor':doctor,
                'page_title': doctor.name,
                'educations': educations,
                'comments':comments,
                'allcomments':allcomments,
                'pointavg':pointavg,
              
                


                "onepoint": onepoint,
                "twopoint": twopoint,
                "threepoint": threepoint,
                "fourpoint": fourpoint,
                
                "fivepoint": fivepoint,
                
                
                
                }
    return render(request,'doctor.html',context)

 

def search(request, keyword):
    doctors  = Doctor.objects.all().filter(name=keyword)
    department = Department.objects.all().filter(name=keyword)

    cout_result =   doctors.count() + department.count()
    if cout_result == 1:
        if doctors.count()==1:
            doctors = Doctor.objects.get(name=keyword)
            context = {'doctor': doctors, 'page_title': doctors.name }
            return render(request,'doctor.html', context)
        if department.count() == 1:
            return HttpResponse('sdfg')
    else:
        context = {'doctors': doctors, 'search_key':keyword
        }
        return render(request,'searchresult.html', context)

def test(request):
    test = request.POST.get('test')
    print(test)
    user = authenticate(request, username="test222222", password="matkhau123")
    if user is not None:
        return HttpResponse("login thanh cong")
    return render(request, 'test.html',context={'test':test})



def loginfinddoctor(request):

    if request.method == 'POST':
  
        inputusername = request.POST.get('username')
        inputpassword = request.POST.get('password')
        user = authenticate(username = inputusername, password = inputpassword)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('unsucess')
    return render(request, 'login.html')

def logoutfinddoctor(request):
    logout(request)
    return redirect('home')
   


def register(request):
    return render(request, 'register.html')

def bookappointment(request, doctor_id):
    
    doctor = Doctor.objects.get(pk=doctor_id)

   
    
    context = {'doctor': doctor,'page_title': doctor.name ,'page_navbar': 'green'}
    if request.method == 'POST':
        ordername = request.POST.get('ordername')
        orderphone = request.POST.get('orderphone')
        date = request.POST.get('date')
        time = request.POST.get('time')
        description = request.POST.get('description')
        user = User.objects.get(pk = request.user.id)
        newbook = BookApartment(ordername=ordername, orderphone=orderphone, description=description,time=time, date=date, user=user, doctor=doctor)
        newbook.save()

        rannumber = random.randint(100000,999999)
        newappointment = AppointMent(user=user, bookapartment=BookApartment.objects.latest('id'), doctor = doctor, vertify_code=rannumber)
        newappointment.save()


        orderinfo = BookApartment.objects.latest('id')
        context.update({'orderinfo': orderinfo})

        return redirect('bookappointmentsuccess')

        # return render(request, 'bookappointmentsuccess.html', context  )
    return render(request, 'bookappointment.html', context)

def bookappointmenthome(request):
    context = {}
    if request.method == 'POST':
        ordername = request.POST.get('ordername')
        orderphone = request.POST.get('orderphone')
        date = request.POST.get('date')
        time = request.POST.get('time')
        description = request.POST.get('description')
        user = User.objects.get(pk = request.user.id)
        
        newbook = BookApartment(ordername=ordername, orderphone=orderphone, description=description,time=time, date=date, user=user)
        newbook.save()

        return redirect('bookappointmentsuccess')
    

 
    context.update({
        'page_title': 'Đăng ký khám' ,'page_navbar': 'green'
    })
    return render(request, 'bookappointmenthome.html', context)

def bookappointmentsuccess(request):
    context = {}

    orderinfo = BookApartment.objects.latest('id')

    verifycode = AppointMent.objects.all().filter(bookapartment=orderinfo)
    if verifycode:
        context = {'verifycode':verifycode[0].vertify_code}
   
    doctor = orderinfo.doctor
    context.update ({
        'orderinfo': orderinfo,
        'doctor': doctor,
    }
    )
    return render(request, 'bookappointmentsuccess.html', context)

def bookappointmentsuccesswithdoctor(request,doctor_id):

    orderinfo = BookApartment.objects.latest('id')

    context = {
        'orderinfo': orderinfo

    }
    return render(request, 'bookappointmentsuccess.html', context)

def appointment(request):

    if request.user.is_authenticated:
        user = User.objects.get(pk = request.user.id)
        appointment = BookApartment.objects.all().filter(user=user)
        context = {'page_title': 'Lịch khám' ,'page_navbar': 'green'
        ,'appointments': appointment}
        return render(request, 'appointment.html',context)

    else:
        return redirect('login')


def appointmentdetail(request,bookappointment_id):
    context = {}

    orderinfo = BookApartment.objects.get(pk=bookappointment_id)

    verifycode = AppointMent.objects.all().filter(bookapartment=orderinfo)
    if verifycode:
        context = {'verifycode':verifycode[0].vertify_code}
   
    doctor = orderinfo.doctor
    context.update ({
        'orderinfo': orderinfo,
        'doctor': doctor,
    }
    )
    return render(request, 'appointmentdetail.html', context)