from django.db import models

# Create your models here.

class Student(models.Model):
    student_name = models.CharField(max_length=30)
    
    
    def __str__(self):
        return str(self.student_name)
    
class Marks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True, related_name='student_marks')
    student_marks = models.CharField(max_length=30)
    def __str__(self):
        return str(self.student_marks)