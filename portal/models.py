from django.db import models

# Create your models here.

class Teacher(models.Model):
    name = models.CharField(null=False , max_length=100)
    username = models.CharField(null=False, unique=True , max_length=150)
    password = models.CharField(null= False , max_length=200)
    salt = models.CharField(null=False , max_length=200)

    def __str__(self):
        return self.username
    
class Student(models.Model):
    name = models.CharField(null=False , max_length=100)
    subject = models.CharField(null=False , max_length=100)
    marks = models.PositiveIntegerField(null=False, default=0)

    def __str__(self):
        return f"{self.name} - {self.subject}"
    
    
    def validate_mark(self):
        if not (0 <= self.marks <= 100):
            raise ValueError("Marks must be between 0 and 100")
        
    def save(self, *args, **kwargs):
        self.validate_mark()
        super().save(*args, **kwargs)    


class Audit_Log(models.Model):
    student = models.ForeignKey(Student , on_delete=models.CASCADE , related_name="student_audit")
    subject = models.CharField(null=False , max_length=100)
    old_marks = models.PositiveIntegerField(null= False , default= 0)
    new_marks = models.PositiveIntegerField(null= False, default=0)
    updated_at = models.DateTimeField(auto_now_add=True)