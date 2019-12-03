from django.db import models

# Create your models here.
from career.models import Career, Career_skill, Career_licence, Career_attitude
from member.models import Member


class Audit_career(models.Model):
    userid = models.ForeignKey(Member, on_delete = models.CASCADE)
    career_id = models.ForeignKey(Career, related_name='career_id_name', on_delete = models.CASCADE)
    audit_id = models.CharField(primary_key= True, max_length=100)

    class Meta:
        db_table = "audit_career"



class Audit_personality(models.Model):
    userid = models.ForeignKey(Member, on_delete=models.CASCADE, default='default')
    audit_personality_R = models.FloatField(max_length=10)
    audit_personality_I = models.FloatField(max_length=10)
    audit_personality_A = models.FloatField(max_length=10)
    audit_personality_S = models.FloatField(max_length=10)
    audit_personality_E = models.FloatField(max_length=10)
    audit_personality_C = models.FloatField(max_length=10)

    class Meta:
        db_table = "audit_personality"



class Audit_attitude(models.Model):
    userid = models.ForeignKey(Member, on_delete=models.CASCADE, default='default')
    audit_id = models.ForeignKey(Audit_career, on_delete=models.CASCADE)
    attitude_id = models.ForeignKey(Career_attitude, related_name='attitude_id_name', on_delete=models.CASCADE)
    score = models.IntegerField()

    class Meta:
        db_table = "audit_attitude"



class Audit_skill(models.Model):
    userid = models.ForeignKey(Member, on_delete=models.CASCADE, default='default')
    audit_id = models.ForeignKey(Audit_career, on_delete=models.CASCADE)
    skill_id = models.ForeignKey(Career_skill, related_name='skill_id_name', on_delete=models.CASCADE)
    score = models.IntegerField()

    class Meta:
        db_table = "audit_skill"


class Audit_licence(models.Model):
    userid = models.ForeignKey(Member, on_delete=models.CASCADE, default='default')
    audit_id = models.ForeignKey(Audit_career, on_delete=models.CASCADE)
    licence_id = models.ForeignKey(Career_licence, related_name='licence_id_name', on_delete=models.CASCADE)
    score = models.BooleanField()

    class Meta:
        db_table = "audit_licence"



class Member_love(models.Model):
    userid = models.ForeignKey(Member, on_delete=models.CASCADE)
    career_id = models.ForeignKey(Career, related_name='love_career_id_name', on_delete=models.CASCADE)

    class Meta:
        db_table = "member_love"


class Plan_skill(models.Model):
    userid = models.ForeignKey(Member, on_delete=models.CASCADE, default='default')
    career_skill = models.CharField(max_length=500, default='default')
    skill_type = models.CharField(max_length=500, default='default')
    skill_content = models.CharField(max_length=500, default='default')

    class Meta:
        db_table = "plan_skill"

class Plan_attitude(models.Model):
    userid = models.ForeignKey(Member, on_delete=models.CASCADE, default='default')
    career_attitude = models.CharField(max_length=500, default='default')

    class Meta:
        db_table = "plan_attitude"

class Plan_licence(models.Model):
    userid = models.ForeignKey(Member, on_delete=models.CASCADE, default='default')
    career_licence = models.CharField(max_length=500, default='default')

    class Meta:
        db_table = "plan_licence"