
from django.contrib import admin

from .models import Doctor, Department, Manager,Specialist,Education,University,Directorate,Reward,UserProfile, BookApartment

# Register your models here.


admin.site.register(Doctor)
admin.site.register(Department)
admin.site.register(Manager)
admin.site.register(Specialist)
admin.site.register(Education)
admin.site.register(University)
admin.site.register(Directorate)
admin.site.register(Reward)
admin.site.register(UserProfile)
admin.site.register(BookApartment)

