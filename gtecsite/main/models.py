from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='categories/', blank=True, null=True)  

    def __str__(self):
        return self.name
    
class Course(models.Model):
    COURSE_TYPE_CHOICES = [
        ('certificate', 'G-TEC Certificate'),
        ('diploma', 'G-TEC Diploma'),
        ('master', 'Master Course'),
        ('special', 'G-TEC Special Program'),
        ('sap', 'SAP Course'),
    ]
   
    title=models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='courses/', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='courses')
    details = models.TextField(blank=True, null=True)      # Add this
    duration = models.CharField(max_length=100, blank=True)  # Optional
    course_type = models.CharField(max_length=20, choices=COURSE_TYPE_CHOICES)
    
    def __str__(self):
        return self.title


class Trainer(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    bio = models.TextField()
    photo = models.ImageField(upload_to='trainers/')
