from itertools import chain

import self as self
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib import auth, messages
import random
import time
from django.contrib.auth.hashers import make_password,check_password

from audit.models import Audit_career, Member_love, Audit_personality, Audit_skill, Audit_attitude, Audit_licence, \
  Plan_skill, Plan_licence, Plan_attitude
from career.models import Career, Career_personality
from .models import Member, Teacher

from .member_form import LoginForm, RegistrationForm, MemberInfo


def register(request):
  if request.method == 'POST':
    userid = request.POST.get('userid')
    email = request.POST.get('email')
    password = request.POST.get('password')
    password2 = request.POST.get('password2')
    if password == password2:
      # 對密碼進行加密
      password = make_password(password)
      Member.objects.create(userid=userid, password=password, email=email)
      form_login = LoginForm(request.POST)
      return render(request, 'login.html', {'member_form': form_login})

    else:
      messages.error(request, "兩次密碼不相同!")
      form_register = RegistrationForm()
      return render(request, 'register.html', {'member_form': form_register})

  else:
    form_register = RegistrationForm()
    return render(request, 'register.html', {'member_form': form_register})



def login(request):
  if request.method == 'POST':
    # 如果登入成功，繫結引數到cookie中，set_cookie
    userid = request.POST.get('userid')
    password = request.POST.get('password')
    if Member.objects.filter(userid=userid).exists():
      user = Member.objects.get(userid=userid)
      if check_password(password, user.password):
        # ticket = 'agdoajbfjad'
        ticket = ''
        for i in range(15):
          s = 'abcdefghijklmnopqrstuvwxyz'
          # 獲取隨機的字串
          ticket += random.choice(s)
          now_time = int(time.time())
          ticket = 'TK' + ticket + str(now_time)
        # 繫結令牌到cookie裡面
        # response = HttpResponse()
        request.session['userid'] = userid

        return HttpResponseRedirect('/home/')

      else:
        messages.error(request, "使用者密碼錯誤!")
        # return HttpResponse('使用者密碼錯誤')
        form_login = LoginForm()
        return render(request, 'login.html', {'member_form': form_login})
    else:
      messages.error(request, "使用者不存在!")
      # return HttpResponse('使用者不存在')
      form_login = LoginForm()
      return render(request, 'login.html', {'member_form': form_login})
  else:
    form_login = LoginForm()
    return render(request, 'login.html', {'member_form': form_login})



def logout(request):
  if request.method == 'GET':
    # response = HttpResponse()
    request.session.clear()
    response = HttpResponseRedirect('/home/')
    response.delete_cookie('ticket')
    return response



def memberInfo(request):
  if request.session.has_key('userid'):
    userid = request.session['userid']
    experience = Teacher.objects.filter(userid=userid)
    form_memberInfo = MemberInfo(request.POST)
    context = {'member_form': form_memberInfo, 'experience': experience}
    if request.method == 'POST':
      username = request.POST.get('username')
      email = request.POST.get('email')
      password = request.POST.get('password')
      password2 = request.POST.get('password2')

      if password == password2:
        # 對密碼進行加密
        password = make_password(password)

        Member.objects.filter(userid=userid).update(username=username, password=password, email=email)
        messages.success(request, "個人資料修改成功!")
        return HttpResponseRedirect('/memberInfo/')
      else:
        messages.error(request, "兩次密碼不相同!")
        form_memberInfo = MemberInfo()
        return render(request, 'memberInfo.html', context)    # career_id = Teacher.objects.filter(userid=userid).career_id
    # print(career_id)
    form_memberInfo = MemberInfo(request.POST)
    context = {'member_form': form_memberInfo, 'experience': experience}
    return render(request, 'memberInfo.html', context)
  else:
    return HttpResponseRedirect('/login/')



def experience(request):
  userid = request.session['userid']
  form_memberInfo = MemberInfo(request.POST)
  experience = Teacher.objects.filter(userid=userid)

  if request.method == 'POST':
    member = Member.objects.get(userid=userid)
    field = request.POST.get('field')
    career_name = request.POST.get('career_id')
    year = request.POST.get('year')
    is_empty = all([field, career_name, year])
    if is_empty:
      if Teacher.objects.filter(userid=member, field=field, career_name=career_name).exists():
        messages.error(request, "已有相同的工作經驗了!")
      else:
        Teacher.objects.create(userid=member, field=field, career_name=career_name, year=year)
        is_teacher=True
        Member.objects.filter(userid=userid).update(is_teacher=is_teacher)
        messages.success(request, "新增工作經驗成功!")
      return HttpResponseRedirect('/memberInfo/')
    else:
      messages.error(request, "請確認是否輸入工作經驗及服務年數!")
      return HttpResponseRedirect('/memberInfo/')

  return HttpResponseRedirect('/memberInfo/')


def delete_experience(request):
  userid = request.GET['userid']
  field = request.GET['field']
  career_name = request.GET['career_name']
  year = request.GET['year']
  experience = Teacher.objects.get(userid=userid, field=field, career_name=career_name, year=year)
  experience.delete()
  if not Teacher.objects.filter(userid=userid).exists():
    is_teacher = False
    Member.objects.filter(userid=userid).update(is_teacher=is_teacher)

  return HttpResponseRedirect('/memberInfo/')


def myAudit(request):
  if request.session.has_key('userid'):
    userid = request.session['userid']

    audit = Audit_career.objects.filter(userid=userid)

    return render(request, 'myAudit.html',locals())
  else:
    return HttpResponseRedirect('/login/')



def myAudit_result(request):
  if request.session.has_key('userid'):
    userid = request.session['userid']
    audit_id = request.GET['audit_id']
    request.session['audit_id'] = audit_id


#結果
    content_career = Audit_career.objects.get(audit_id=audit_id)
    career_name = content_career.career_id.career_name
    career = Career.objects.get(career_name=career_name)
    career_id = career.career_id
    print(career_id)
    content_personality = Career_personality.objects.get(career_id=career_id)


    # audit = Audit_career.objects.get(audit_id=audit_id)

    result_personality = Audit_personality.objects.get(userid=userid)

    result_skill_5 = Audit_skill.objects.filter(audit_id=audit_id, score=5)
    result_skill_4 = Audit_skill.objects.filter(audit_id=audit_id, score=4)
    result_skill_3 = Audit_skill.objects.filter(audit_id=audit_id, score=3)
    result_skill_2 = Audit_skill.objects.filter(audit_id=audit_id, score=2)
    result_skill_1 = Audit_skill.objects.filter(audit_id=audit_id, score=1)



    result_attitude_5 = Audit_attitude.objects.filter(audit_id=audit_id, score=5)
    result_attitude_4 = Audit_attitude.objects.filter(audit_id=audit_id, score=4)
    result_attitude_3 = Audit_attitude.objects.filter(audit_id=audit_id, score=3)
    result_attitude_2 = Audit_attitude.objects.filter(audit_id=audit_id, score=2)
    result_attitude_1 = Audit_attitude.objects.filter(audit_id=audit_id, score=1)



    result_licence_true = Audit_licence.objects.filter(audit_id=audit_id, score=True)
    result_licence_false = Audit_licence.objects.filter(audit_id=audit_id, score=False)


    return render(request, 'myAudit_result.html', locals())
  else:
    return HttpResponseRedirect('/login/')



def myCareer(request):
  if request.session.has_key('userid'):
    userid = request.session['userid']
    love = Member_love.objects.filter(userid=userid)
    return render(request, 'myCareer.html',locals())
  else:
    return HttpResponseRedirect('/login/')



def delete_love(request):
  if not request.session.has_key('userid'):
    messages.error(request, "需要進行登入!")
    return HttpResponseRedirect('/login/')

  else:
    userid = request.session['userid']
    career_name = request.GET['career_name']
    career = Career.objects.get(career_name=career_name)
    career_id = career.career_id
    messages.success(request, "取消收藏!")
    Member_love.objects.filter(userid=userid, career_id=career_id).delete()
    return HttpResponseRedirect('/myCareer/')

def addPlan_skill(request):
  if request.session.has_key('userid'):
    userid = request.session['userid']
    member = Member.objects.get(userid=userid)
    career_skill = request.GET['career_skill']
    skill_type = request.GET['skill_type']
    skill_content = request.GET['skill_content']
    audit_id = request.session['audit_id']

    # career_attitude = request.GET['career_attitude']
    # career_licence = request.GET['career_licence']
    if not Plan_skill.objects.filter(userid=userid, career_skill=career_skill, skill_type=skill_type, skill_content=skill_content).exists():
      Plan_skill.objects.create(userid=member, career_skill=career_skill, skill_type=skill_type, skill_content=skill_content)
      messages.success(request, "新增規劃成功!")
    else:
      messages.success(request, "已新增規劃了!")

    return HttpResponseRedirect("/myAudit_result/?audit_id=" + str(audit_id))
  else:
    return HttpResponseRedirect('/login/')


def addPlan_attitude(request):
  if request.session.has_key('userid'):
    userid = request.session['userid']
    member = Member.objects.get(userid=userid)

    audit_id = request.session['audit_id']

    career_attitude = request.GET['career_attitude']
    if not Plan_attitude.objects.filter(userid=userid, career_attitude=career_attitude).exists():
      Plan_attitude.objects.create(userid=member, career_attitude=career_attitude)
      messages.success(request, "新增規劃成功!")
    else:
      messages.success(request, "已新增規劃了!")

    return HttpResponseRedirect("/myAudit_result/?audit_id=" + str(audit_id))
  else:
    return HttpResponseRedirect('/login/')

def addPlan_licence(request):
  if request.session.has_key('userid'):
    userid = request.session['userid']
    member = Member.objects.get(userid=userid)

    audit_id = request.session['audit_id']

    career_licence = request.GET['career_licence']
    if not Plan_licence.objects.filter(userid=userid, career_licence=career_licence).exists():
      Plan_licence.objects.create(userid=member, career_licence=career_licence)
      messages.success(request, "新增規劃成功!")
    else:
      messages.success(request, "已新增規劃了!")

    return HttpResponseRedirect("/myAudit_result/?audit_id=" + str(audit_id))
  else:
    return HttpResponseRedirect('/login/')

def myPlan_skill(request):
  if request.session.has_key('userid'):
    userid = request.session['userid']
    skill_plan = Plan_skill.objects.filter(userid=userid)

    return render(request, 'myPlan_skill.html', locals())
  else:
    return HttpResponseRedirect('/login/')


def myPlan_attitude(request):
  if request.session.has_key('userid'):
    userid = request.session['userid']
    attitude_plan = Plan_attitude.objects.filter(userid=userid)

    return render(request, 'myPlan_attitude.html', locals())
  else:
    return HttpResponseRedirect('/login/')


def myPlan_licence(request):
  if request.session.has_key('userid'):
    userid = request.session['userid']
    licence_plan = Plan_licence.objects.filter(userid=userid)

    return render(request, 'myPlan_licence.html', locals())
  else:
    return HttpResponseRedirect('/login/')

def delete_plan_skill(request):
  if request.session.has_key('userid'):
    userid = request.GET['userid']
    career_skill = request.GET['career_skill']
    skill_type = request.GET['skill_type']
    skill_content = request.GET['skill_content']
    plan_skill = Plan_skill.objects.get(userid=userid, career_skill=career_skill, skill_type=skill_type, skill_content=skill_content)
    plan_skill.delete()
    messages.success(request, "已完成，從規畫表中移除!")
    return HttpResponseRedirect('/myPlan_skill/')

  else:
    return HttpResponseRedirect('/login/')


def delete_plan_attitude(request):
  if request.session.has_key('userid'):
    userid = request.GET['userid']
    career_attitude = request.GET['career_attitude']
    plan_attitude = Plan_attitude.objects.get(userid=userid, career_attitude=career_attitude)
    plan_attitude.delete()
    messages.success(request, "已完成，從規畫表中移除!")
    return HttpResponseRedirect('/myPlan_attitude/')

  else:
    return HttpResponseRedirect('/login/')


def delete_plan_licence(request):
  if request.session.has_key('userid'):
    userid = request.GET['userid']
    career_licence = request.GET['career_licence']
    plan_licence = Plan_licence.objects.get(userid=userid, career_licence=career_licence)
    plan_licence.delete()
    messages.success(request, "已完成，從規畫表中移除!")
    return HttpResponseRedirect('/myPlan_licence/')

  else:
    return HttpResponseRedirect('/login/')
