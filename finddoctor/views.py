import datetime
from django.utils import timezone

from django.shortcuts import render,get_object_or_404
from django.shortcuts import redirect

from django.shortcuts import HttpResponse

from .models import *
from itertools import chain
from django.contrib.auth import authenticate,login,logout


from django.contrib.auth.models import User

from django.db.models import Avg


from django.core.files.storage import FileSystemStorage

from django.http import Http404


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

    top_doctors_list = Doctor.objects.all().filter(showinhome=True)
    top_departments_list = Department.objects.all().filter(showinhome=True)
    top_doctors_list_id = []
    for i in top_doctors_list:
        top_doctors_list_id.append(i.id)
    top_doctors_education = Education.objects.all().filter(doctor_id__in=top_doctors_list_id).filter(main=True)

    asks = AskDoctor.objects.all().order_by('-pk')[:5]
    answer = Answer.objects.all().filter(ask__in=asks)
    
    context.update({'top_doctors_list': top_doctors_list,
                'doctor_names':doctor_names,
                'top_doctors_education':  top_doctors_education,
                'page_title': "Trang chủ",
                'top_departments_list':  top_departments_list,
                'asks': asks,
                'answer': answer
    })
    if request.method == 'POST':
            ask = request.POST.get('ask')
            user = User.objects.get(pk = request.user.id)
            photo = None
            
            if bool(request.FILES.get('photo', False)) == True:

                    myfile = request.FILES['photo']
                    fs = FileSystemStorage(location='media/imgs/asks/')
                    filename = fs.save(myfile.name, myfile)
                    photo = '/imgs/asks/' + str(filename)

            newask = AskDoctor(ask=ask, user=user, photo = photo)
            newask.save()
            return redirect('home')

    return render(request,'index.html', context)


def doctor(request, doctor_id):
    verify_code = 0
    doctor = Doctor.objects.get(pk=doctor_id)
    countappointmentdone = BookApartment.objects.all().filter(doctor=doctor).filter(isdone='Đã khám xong').count()
    context = {'countappointmentdone': countappointmentdone}
    if request.user.is_authenticated:
            verify_code = 0
            user = User.objects.get(pk = request.user.id)
            amplist = BookApartment.objects.all().filter(doctor=doctor,user=user,isdone='Đã khám xong')
            deobietdattenlagi = AppointMent.objects.all().filter(bookapartment__in=amplist)
            otplist = VerifyCode.objects.all().filter(appointment__in=deobietdattenlagi)
            if otplist:
                verify_code = otplist[0].vertify_code
                context.update({
                'verify_code':verify_code,}) 
    if request.method == 'POST':
        verify = False
        points = request.POST.get('points')
        if points is None:
            points = 3
        comment = request.POST.get('comment')
        user = User.objects.get(pk = request.user.id)
        if verify_code != 0:
            if verify_code == int(request.POST.get('otp')):
                    verify = True
                    VerifyCode.objects.filter(vertify_code=verify_code).delete()
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

    speciallist = Specialist.objects.all().filter(doctor=doctor)

    manager = Manager.objects.all().filter(doctor=doctor)

  
    context.update ({ 'doctor':doctor,
                'page_title': doctor.name,
                'educations': educations,
                'comments':comments,
                'allcomments':allcomments,
                'point_avg':pointavg,
                'speciallist': speciallist,
                'manager': manager,
                


                "onepoint": onepoint,
                "twopoint": twopoint,
                "threepoint": threepoint,
                "fourpoint": fourpoint,
                
                "fivepoint": fivepoint,
                
                
                
                }
    )
    try:
        directori = Directorate.objects.all().get(doctor=doctor)
        context.update({'directori': directori})
    except:
        pass

    if doctor.user:
        user = doctor.user
        countanswer = Answer.objects.all().filter(user=user).count()
        context.update({'countanswer': countanswer})

   
    return render(request,'doctor.html',context)

 

def search(request, keyword):
    try:
        doctors  = Doctor.objects.get(name=keyword)

        return redirect('doctor', doctors.id)
    except:
        return redirect('404page')

def test(request):
    test = request.POST.get('test')
    print(test)
    user = authenticate(request, username="test222222", password="matkhau123")
    if user is not None:
        return HttpResponse("login thanh cong")
    return render(request, 'test.html',context={'test':test})



def loginfinddoctor(request):
    user = User.objects.all()
    allusername = []
    for i in user:
        allusername.append(i.username)
    context = {'allusername':allusername}

    if request.method == 'POST':
  
        inputusername = request.POST.get('phone')
        inputpassword = request.POST.get('password')
        user = authenticate(username = inputusername, password = inputpassword)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            context.update({
                            'lastphone': inputusername})
            return render(request,'login.html',context)
    return render(request, 'login.html', context)

def logoutfinddoctor(request):
    logout(request)
    return redirect('home')
   


def register(request):
    user = User.objects.all()
    allusername = []
    for i in user:
        allusername.append(i.username)

    if request.method == 'POST':
        phone = request.POST.get('phone')
        password = request.POST.get('password')

        try:
            newuser = User.objects.create_user(phone, 'lennon@thebeatles.com',password)
            newuser.save()
            newuserprofile = UserProfile(user=newuser, avatar = 'imgs/noavatar.jpg',name=phone)
            newuserprofile.save()
            user = authenticate(username = phone, password = password)
            if user is not None:
                login(request, user)
                return redirect ('profile')
        except:
       # raise exception or error message
            return HttpResponse('<h1>Không thành công. Tài khoản này đã tồn tại</h1>')


        return redirect('login')
    context = {'allusername': allusername,

                
    }
    return render(request, 'register.html', context)

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
        newappointment = AppointMent(user=user, bookapartment=BookApartment.objects.latest('id'), doctor = doctor)
        newappointment.save()
        verify = VerifyCode(appointment=newappointment,vertify_code=rannumber)
        verify.save()
        orderinfo = BookApartment.objects.latest('id')
        context.update({'orderinfo': orderinfo})
        return redirect('bookappointmentsuccess')
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
        newappointment = AppointMent(user=user,bookapartment=newbook)
        newappointment.save()
        rannumber = random.randint(100000,999999)
        verify = VerifyCode(appointment=newappointment,vertify_code=rannumber)
        verify.save()

      

        return redirect('bookappointmentsuccess')
    

 
    context.update({
        'page_title': 'Đăng ký khám' ,'page_navbar': 'green'
    })
    return render(request, 'bookappointmenthome.html', context)

def bookappointmentsuccess(request):
    context = {}

    orderinfo = BookApartment.objects.latest('id')

    # verifycode = AppointMent.objects.all().filter(bookapartment=orderinfo)
    # if verifycode:
    #     context = {'verifycode':verifycode[0].vertify_code}
   
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
        context = {'page_title': 'Lịch khám' 
        ,'appointments': appointment}
        countwait = appointment.filter(isdone='Đang chờ khám').count()
        countdone = appointment.filter(isdone='Đã khám xong').count()
        countcancel = appointment.filter(isdone='Đã huỷ').count()
        context.update({'countwait': countwait, 'countdone': countdone, 'countcancel': countcancel})
        return render(request, 'appointment.html',context)

    else:
        return redirect('login')


def appointmentdetail(request,bookappointment_id):
    context = {}

    orderinfo = BookApartment.objects.get(pk=bookappointment_id)

    if orderinfo.isdone == 'Đã khám xong':
        appointment = AppointMent.objects.get(bookapartment=orderinfo)
        # try:
        #     verify = VerifyCode.objects.get(appointment=appointment)
        #     verifycode = verify.vertify_code
        #     context.update({'verifycode': verifycode})
        # except:
        #     pass
    
   
    doctor = orderinfo.doctor
    context.update ({
        'orderinfo': orderinfo,
        'doctor': doctor,
    }
    )
    return render(request, 'appointmentdetail.html', context)

def profile(request):
    
    context = {'page_title': 'Thông tin tài khoản'}

    if request.user.is_authenticated:
        user_id = request.user.id
        if request.method == 'POST' :
            name = request.POST.get('name')
            user = User.objects.get(pk=user_id)
            updateprofile = UserProfile.objects.get(user=user)

           

        

            if bool(request.FILES.get('avatar', False)) == True:
                print('-------')

                myfile = request.FILES['avatar']
                fs = FileSystemStorage(location='media/imgs/avatars/')
                filename = fs.save(myfile.name, myfile)
                avatar = '/imgs/avatars/' + str(filename)
                updateprofile.avatar = avatar
                updateprofile.save()
      
            try:
                updateprofile.name = name
                updateprofile.save()
                return redirect('profile')
            except:
                return HttpResponse('Lỗi!')
        return render(request, 'profile.html', context)
    else:
        return HttpResponse('Vui lòng đăng nhập')


def mycomment(request):
    if request.user.is_authenticated:
        context = {'page_title': 'Đánh giá của tôi'}
        user = User.objects.get(id = request.user.id)
        comments = ReviewDoctor.objects.all().filter(user=user)
        context.update({'comments':comments})
        return render (request, 'mycomment.html', context)
    else:
        return HttpResponse('Vui lòng đăng nhập')

def alldoctors(request):
    context = {'page_title': 'Tất cả bác sĩ'}
    doctors = Doctor.objects.all()
    educations = Education.objects.all()
    context.update({'doctors':doctors, 'educations': educations})
    return render(request, 'alldoctors.html', context)

def department(request, department_id):
    
    try:
        department = Department.objects.get(pk=department_id)
        doctors = Manager.objects.all().filter(department=department)
        
        manager = doctors.filter(role='Trưởng khoa')
        educations = Education.objects.all()
        context = {'page_title': department.name, 'department':department, 'doctors': doctors,'educations': educations}

        if manager:
            managername = manager[0].doctor
            context.update({'manager': managername})

  

        return render(request, 'department.html', context)


    except Department.DoesNotExist:
        return redirect('page404')

def ask(request, ask_id):
    context = {'page_title': 'Hỏi bác sĩ','page_navbar': 'green'}
    try:
        ask = AskDoctor.objects.get(pk=ask_id)
        answer = Answer.objects.all().filter(ask=ask)
   
        context.update({'ask': ask,'answer':answer})

        if request.method == 'POST':
            answer = request.POST.get('answer')
            user = User.objects.get(pk = request.user.id)
            newanswer = Answer(ask=ask, user=user, answer=answer)
            newanswer.save()
            ask.isanswer = True
            ask.save()
            return redirect('ask',ask_id)

            # if bool(request.FILES.get('photo', False)) == True:

            #         myfile = request.FILES['photo']
            #         fs = FileSystemStorage(location='media/imgs/asks/')
            #         filename = fs.save(myfile.name, myfile)
            #         photo = '/imgs/asks/' + str(filename)
        else:
            return render(request, 'ask.html', context)

    except:
        return redirect('page404')

def page404(request):
    return render(request,'404.html')

def alldepartments(request):
    context = {}
    departments = Department.objects.all()
    context.update({'top_departments_list': departments, 'page_title':'Tất cả chuyên khoa'})
    return render(request, 'alldepartments.html', context)

def allasks(request):
    context = {}
    asks = AskDoctor.objects.all().order_by('-pk')
    countanswered = asks.filter(isanswer = True).count()
    countnotanswered = asks.filter(isanswer = False).count()
    if request.method == 'POST':
            ask = request.POST.get('ask')
            user = User.objects.get(pk = request.user.id)
            photo = None
            
            if bool(request.FILES.get('photo', False)) == True:

                    myfile = request.FILES['photo']
                    fs = FileSystemStorage(location='media/imgs/asks/')
                    filename = fs.save(myfile.name, myfile)
                    photo = '/imgs/asks/' + str(filename)

            newask = AskDoctor(ask=ask, user=user, photo = photo)
            newask.save()
            return redirect('allasks')
    
    context.update({'asks': asks, 'page_title':'Tất cả câu hỏi','countanswered':countanswered,'countnotanswered':countnotanswered})
    return render(request, 'allasks.html', context)
   
def about(request):
    context = {'page_title':'About'}

    return render(request, 'staticpage/about.html', context)

def myasks(request):
    context = {'page_title': 'Danh sách câu hỏi'}
    try:
        user = User.objects.get(pk = request.user.id )
        asks = AskDoctor.objects.all().filter(user = user).order_by('-pk')
        context.update({'asks': asks})
    except:
        return redirect('page404')
    return render(request, 'myasks.html', context)
