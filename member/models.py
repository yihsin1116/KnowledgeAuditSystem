from django.db import models

# Create your models here.


class Member(models.Model):
    userid = models.CharField(primary_key= True, max_length=100)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    is_teacher = models.BooleanField( default = False )

    class Meta:
        db_table = "member"


class Teacher(models.Model):
    userid = models.ForeignKey(Member, on_delete=models.CASCADE)
    field = models.CharField(max_length=100)
    career_name = models.CharField(max_length=100)
    year = models.CharField(max_length=100)

    class Meta:
        db_table = "teacher"
