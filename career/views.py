import time, datetime

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from audit.models import Member_love
from career.models import Career, Career_info, Career_skill, Career_licence, Career_personality, Career_fucture, Career_attitude, Message
from member.member_form import LoginForm
from member.models import Member


def search(request):
  network = Career.objects.all().filter(field="網路管理")
  system = Career.objects.all().filter(field="系統規劃")
  software = Career.objects.all().filter(field="軟體工程")
  eb =  Career.objects.all().filter(field="電子商務")
  management =  Career.objects.all().filter(field="分析管理")

  return render(request, 'search.html', locals())



def career(request):
  network = Career.objects.all().filter(field="網路管理")
  system = Career.objects.all().filter(field="系統規劃")
  software = Career.objects.all().filter(field="軟體工程")
  eb = Career.objects.all().filter(field="電子商務")
  management = Career.objects.all().filter(field="分析管理")
  career_id = request.GET['career_id']
  request.session['career_id'] = career_id
  print(career_id)

  content_career = Career.objects.get(career_id=career_id)
  content_info = Career_info.objects.all().filter(career_id=career_id)
  content_personality = Career_personality.objects.all().filter(career_id=career_id)
  content_skill = Career_skill.objects.all().filter(career_id=career_id)
  content_attitude = Career_attitude.objects.all().filter(career_id=career_id)
  content_licence = Career_licence.objects.all().filter(career_id=career_id)
  content_fucture = Career_fucture.objects.all().filter(career_id=career_id)

  message = Message.objects.all().filter(career_id=career_id)

  return render(request, 'career.html', locals())



def love(request):
  if not request.session.has_key('userid'):
    messages.error(request, "需要登入才能進行收藏!")
    return HttpResponseRedirect('/login/')

  else:
    userid = request.session['userid']
    member = Member.objects.get(userid=userid)
    career_id = request.session['career_id']
    career = Career.objects.get(career_id=career_id)

    if Member_love.objects.filter(userid=member, career_id=career).exists():
      Member_love.objects.filter(userid=member, career_id=career).delete()
      messages.success(request, "取消收藏!")
    else:
      Member_love.objects.create(userid=member, career_id=career)
      messages.success(request, "新增至收藏!")

    return HttpResponseRedirect("/career/?career_id=" + str(career_id))



def add(request):
  career_id = request.session['career_id']
  if not request.session.has_key('userid'):
    return HttpResponseRedirect('/login/')

  else:
    userid = request.session['userid']
    if Member.objects.get(userid=userid).is_teacher:
      career_id = request.session['career_id']
      content_career = Career.objects.get(career_id=career_id)
      content_skill = Career_skill.objects.filter(career_id=career_id)
      print(content_skill)

      return render(request, 'add_career_content.html', locals())
    else:
      messages.success(request, "需為老師身分才能為職業職能新增內容!")
      return HttpResponseRedirect("/career/?career_id=" + str(career_id))



def addCareer(request):
  if not request.session.has_key('userid'):
    return HttpResponseRedirect('/login/')

  else:
    userid = request.session['userid']
    career_id = request.session['career_id']
    career = Career.objects.get(career_id=career_id)

    if Member.objects.get(userid=userid).is_teacher:
      if request.method == 'POST':
        career_info = request.POST.get('career_info')
        is_empty = all([career_info])
        if is_empty:
          Career_info.objects.create(career_id=career, career_info=career_info)

        career_fucture = request.POST.get('career_fucture')
        is_empty = all([career_fucture])
        if is_empty:
          Career_fucture.objects.create(career_id=career, career_fucture=career_fucture)

        career_skill = request.POST.get('career_skill')
        skill_type = request.POST.get('skill_type')
        skill_content = request.POST.get('skill_content')
        is_empty = all([career_skill, skill_type, skill_content])
        if is_empty:
          Career_skill.objects.create(career_id=career, career_skill=career_skill, skill_type=skill_type, skill_content=skill_content)

        career_attitude = request.POST.get('career_attitude')
        is_empty = all([career_attitude])
        if is_empty:
          Career_attitude.objects.create(career_id=career, career_attitude=career_attitude)

        career_licence = request.POST.get('career_licence')
        is_empty = all([career_licence])
        if is_empty:
          Career_licence.objects.create(career_id=career, career_licence=career_licence)

        messages.success(request, "新增成功!")

        return render(request, 'add_success.html', locals())
    else:
      messages.success(request, "需為老師身分才能為職業職能新增內容!")
      return HttpResponseRedirect("/career/?career_id=" + str(career_id))


def message(request):
  if not request.session.has_key('userid'):
    messages.error(request, "需要登入才能進行留言!")
    return HttpResponseRedirect('/login/')

  else:
    userid = request.session['userid']
    career_id = request.session['career_id']
    content = request.POST.get('content')
    career = Career.objects.get(career_id=career_id)
    time = datetime.datetime.now()
    message_id = userid + str(time)

    Message.objects.create(career_id=career, message_id=message_id, userid=userid, content=content, time=time)

    return HttpResponseRedirect("/career/?career_id=" + str(career_id))

def myCareer_result(request):
  network = Career.objects.all().filter(field="網路管理")
  system = Career.objects.all().filter(field="系統規劃")
  software = Career.objects.all().filter(field="軟體工程")
  eb = Career.objects.all().filter(field="電子商務")
  management = Career.objects.all().filter(field="分析管理")
  career_name = request.GET['career_name']
  career_id = Career.objects.get(career_name=career_name)
  print(career_id)

  content_career = Career.objects.get(career_id=career_id)
  content_info = Career_info.objects.all().filter(career_id=career_id)
  content_personility = Career_personality.objects.all().filter(career_id=career_id)
  content_skill = Career_skill.objects.all().filter(career_id=career_id)
  content_attitude = Career_attitude.objects.all().filter(career_id=career_id)
  content_licence = Career_licence.objects.all().filter(career_id=career_id)
  content_fucture = Career_fucture.objects.all().filter(career_id=career_id)

  message = Message.objects.all().filter(career_id=career_id)

  return render(request, 'myCareer_result.html', locals())


