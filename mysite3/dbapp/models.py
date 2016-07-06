from django.db import models

# Create your models here.
class Department(models.Model):
   dept_name=models.CharField(max_length=200)
   def __str__(self):
      return self.dept_name
class Student(models.Model):
   dept_name=models.ForeignKey(Department)
   student_name=models.CharField(max_length=200)
   usn=models.CharField(max_length=200)
   project_completed=models.CharField(max_length=200)
   def __str__(self):
      return self.student_name