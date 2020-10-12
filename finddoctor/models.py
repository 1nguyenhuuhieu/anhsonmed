from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Doctor(models.Model):
    name = models.CharField(max_length=200)
    avatar = models.ImageField(upload_to = 'imgs/avatars/',null=True, blank=True)

    showinhome = models.BooleanField(default=False, help_text="Có xuất hiện ở mục bác sĩ nổi bật tại trang chủ")
   


    
    birth_of_date = models.DateField()
    description = models.TextField(null=True, blank=True)

    highlight = models.CharField(max_length=200, null=True, blank=True )

  

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    created_date = models.DateField()
    avatar = models.ImageField(upload_to = 'imgs/avatars/',null=True, blank=True)
    showinhome = models.BooleanField(default=False, help_text="Có xuất hiện ở mục nổi bật tại trang chủ")
    def __str__(self):
        return self.name

class Manager(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    role_list = (
        ('TK', 'Trưởng Khoa'),
        ('PK', 'Phó Khoa'),
        ('DDT', 'Điều dưỡng trưởng'),
    )
    role = models.CharField(max_length=200, choices=role_list)

    def __str__(self):
        return str(self.doctor) + '--'+ str(self.department) + '--'+str(self.role)

class Directorate(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    role_list = (
        ('GĐ', 'Giám Đốc'),
        ('PGĐ', 'Phó Giám Đốc'),
    )
    role = models.CharField(max_length=200, choices=role_list)

    def __str__(self):
        return self.doctor + self.role


class Specialist(models.Model):
    title = models.CharField(max_length=200)
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Reward(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    def __str__(self):
        return self.title



class University(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Education(models.Model):
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    certified_date = models.DateField()
    certified_by = models.ForeignKey(University, on_delete=models.CASCADE)
    main = models.BooleanField(default=False)
    def __str__(self):
        return str(self.title) + '-----'+ str(self.doctor) 



