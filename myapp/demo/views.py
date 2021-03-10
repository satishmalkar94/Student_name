from django.shortcuts import render
from .models import Student,Marks


# # Create your views here.
# def student_view(request):
#     student = Student.objects.all()
#     mar = Marks.objects.all()
#     # context = {
#     #     'student_name':obj.student_name,
       
        
#     # }
    
#     student = {
        
#         'student':student
#     }
#     mar = {
#         'mar':mar
#     }
#     return render(request,'result.html',student,mar)



def marks_view(request):
    mar = Marks.objects.all()
    # context = {
    #     'student_marks':obj.student_marks
        
    # }
    mar = {
        
        'mar':mar
    }
    return render(request,'result.html',mar)
