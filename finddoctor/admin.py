
from django.contrib import admin

from .models import *

class EducationInline(admin.StackedInline):
    model = Education
    extra = 1



class DoctorAdmin(admin.ModelAdmin):

    fieldsets = [
    (None,               {'fields':  ['name', 'avatar', 'showinhome', 'birth_of_date', 'description', 'highlight']}),
    ]

    inlines = [EducationInline]

# Register your models here.


admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Department)
admin.site.register(Manager)
admin.site.register(Specialist)
admin.site.register(Education)
admin.site.register(University)
admin.site.register(Directorate)
admin.site.register(Reward)
admin.site.register(UserProfile)
admin.site.register(BookApartment)
admin.site.register(ReviewDoctor)
admin.site.register(AppointMent)
admin.site.register(VerifyCode)

