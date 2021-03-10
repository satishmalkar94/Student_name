from django.contrib import admin
from .models import Student,Marks


# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Student, StudentAdmin)

class MarksAdmin(admin.ModelAdmin):
    pass
admin.site.register(Marks, MarksAdmin)