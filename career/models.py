from datetime import timezone

from django.db import models
import member.models
# Create your models here.



class Career(models.Model):
    career_id = models.CharField(primary_key=True, max_length=100)
    career_name = models.CharField(max_length=100) #專案管理師
    field = models.CharField(max_length=100) #分析管理
    career_type = models.CharField(max_length=100) #分析與管理#技術#助理

    class Meta:
        db_table = "career"



class Career_info(models.Model):
    career_id = models.ForeignKey(Career, on_delete = models.CASCADE)
    career_info = models.CharField(max_length=500)

    class Meta:
        db_table = "career_info"



class Career_personality(models.Model):
    career_id = models.ForeignKey(Career, on_delete = models.CASCADE)
    personality_R = models.FloatField(max_length=10)
    personality_I = models.FloatField(max_length=10)
    personality_A = models.FloatField(max_length=10)
    personality_S = models.FloatField(max_length=10)
    personality_E = models.FloatField(max_length=10)
    personality_C = models.FloatField(max_length=10)

    class Meta:
        db_table = "career_personality"




class Career_attitude(models.Model):
    career_id = models.ForeignKey(Career, on_delete = models.CASCADE)
    attitude_id = models.AutoField(primary_key=True, max_length=100)
    career_attitude = models.CharField(max_length=100)

    class Meta:
        db_table = "career_attitude"



class Career_skill(models.Model):
    career_id = models.ForeignKey(Career, on_delete = models.CASCADE)
    skill_id = models.AutoField(primary_key=True, max_length=180)
    career_skill = models.CharField(max_length=100)
    skill_type = models.CharField(max_length=100)
    skill_content = models.CharField(max_length=140)

    class Meta:
        db_table = "career_skill"


class Career_licence(models.Model):
    licence_id = models.AutoField(primary_key=True, max_length=180)
    career_id = models.ForeignKey(Career, on_delete=models.CASCADE)
    career_licence = models.CharField(max_length=100)

    class Meta:
        db_table = "career_licence"



class Career_fucture(models.Model):
    career_id = models.ForeignKey(Career, on_delete = models.CASCADE)
    career_fucture = models.CharField(max_length=100)

    class Meta:
        db_table = "career_fucture"



class Message(models.Model):
    userid = models.CharField(max_length=100)
    career_id  = models.ForeignKey(Career, on_delete = models.CASCADE)
    message_id = models.CharField(primary_key=True, max_length=100)
    content  = models.CharField(max_length=200)
    time = models.DateTimeField()
    class Meta:
        db_table = "message"