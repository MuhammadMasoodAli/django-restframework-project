from enum import unique
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Create your models here.

# 1.Course Model
class Course(models.Model):
    name = models.CharField(max_length = 100)
    duration = models.IntegerField()

    def __str__(self):
        return self.name
        

# 2.Student Model
class Student(models.Model):
     name = models.CharField(max_length = 100)
     email = models.EmailField(unique = True)
     age = models.IntegerField()
     course = models.ForeignKey(Course, on_delete= models.CASCADE)
     created_at = models.DateTimeField(auto_now_add=True)

     def __str__(self):
        return self.name


# 3. Profile Model
class Profile(models.Model):

    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')

    def __str__(self):
        return f"{self.user.username} - {self.role}"


# Signal To Create Profile Automatically When User Created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)