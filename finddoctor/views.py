from django.shortcuts import render
from django.shortcuts import redirect

from django.shortcuts import HttpResponse

from .models import Doctor,Department,Education, UserProfile
from itertools import chain
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def index(request):
  
    user_id = request.user.id
    if user_id:
        user_avatar = UserProfile.objects.get(pk=user_id)
        if user_avatar.avatar :
            context = {'user_avatar': user_avatar.avatar}

        else:
            print('khong co anh')
            context = {'user_avatar': '/imgs/noavatar.jpg'}
    else:
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
    educations = Education.objects.all().filter(doctor_id = doctor_id)
    context = {'doctor':doctor,
                'page_title': doctor.name,
                'educations': educations}
    return render(request,'doctor.html',context)

def search(request, keyword):
    doctors  = Doctor.objects.all().filter(name=keyword)
    department = Department.objects.all().filter(name=keyword)

    cout_result =   doctors.count() + department.count()
    if cout_result == 1:
        if doctors.count()==1:
            doctors = Doctor.objects.get(name=keyword)
            context = {'doctor': doctors}
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
        print(inputusername)
        print(inputpassword)
        user = authenticate(username = inputusername, password = inputpassword)
        if user is not None:
            login(request, user)

            return redirect('home')
        else:
            return HttpResponse('unsucess')
    return render(request, 'login.html')
   


def register(request):
    return render(request, 'register.html')

def bookappointment(request, doctor_id):
    doctor = Doctor.objects.get(pk=doctor_id)
    context = {'doctor':doctor}
    return render(request, 'bookappointment.html',context)
def bookappointmenthome(request):
    context = {
        'page_title': 'Đăng ký khám'
    }
    return render(request, 'bookappointmenthome.html', context)