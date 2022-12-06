from django.db import models

# Create your models here.
group = (
    ('A+','A+'),
    ('O+','O+'),
    ('B+','B+'),
    ('AB+','AB+'),
    ('A-','A-'),
    ('O-','O-'),
    ('B-','B-'),
    ('AB-','AB-'),
)

class Employee(models.Model):

    
    UserName = models.CharField(max_length=200)
    Email = models.EmailField()
    Department = models.CharField(max_length=200)
    Designation = models.CharField(max_length=200)
    
    EmergencyContact=models.CharField(max_length=10)
    BloodGroup=models.CharField(max_length=200)
    dob=models.DateField()
    WorkLocation=models.CharField(max_length=200)
    Address=models.TextField(max_length=200)
    martialstatus_choices=(('single','Single'),('married','Married'),)
    MaritalStatus = models.CharField(max_length=50,choices=martialstatus_choices)
   