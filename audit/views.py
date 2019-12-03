from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from audit.models import Audit_career, Audit_personality, Audit_skill, Audit_attitude, Audit_licence
from career.models import Career_personality, Career_skill, Career_attitude, Career_licence, Career
from member.member_form import LoginForm
# from  audit.memberInfo_form import MemberInfo
from member.models import Member


def audit_personality(request):
  if request.session.has_key('userid'):

    userid = request.session['userid']
    member = Member.objects.get(userid=userid)
    career_id = request.GET['career_id']
    audit_id = userid + str(career_id)
    request.session['audit_id'] =audit_id
    messages.success(request, "第一部分為性向職類，第二部分：知識技能，第三部分：職務能力，第四部分：相關證照")
    content_career = Career.objects.get(career_id=career_id)
    content_personality = Career_personality.objects.all().filter(career_id=career_id)

    if not Audit_personality.objects.filter(userid=userid):
        return render(request, 'audit_personality.html', locals())
    else:
        audit_personality = Audit_personality.objects.get(userid=userid)
        return render(request, 'audit_personality.html', locals())



  else:
    return HttpResponseRedirect('/login/')


def audit_skill(request):
  if request.session.has_key('userid'):
    audit_id = request.session['audit_id']
    userid = request.session['userid']
    member = Member.objects.get(userid=userid)
    career_id = request.GET['career_id']
    career = Career.objects.get(career_id=career_id)
    if not Audit_personality.objects.filter(userid=userid):
        messages.error(request, "尚未新增性向職類")
        return HttpResponseRedirect('/audit_personality/?career_id=' + str(career_id))

    if request.method == 'POST':
      audit_personality_R = request.POST.get('audit_personality_R')
      audit_personality_I = request.POST.get('audit_personality_I')
      audit_personality_A = request.POST.get('audit_personality_A')
      audit_personality_S = request.POST.get('audit_personality_S')
      audit_personality_E = request.POST.get('audit_personality_E')
      audit_personality_C = request.POST.get('audit_personality_C')

      if Audit_personality.objects.get(userid=userid):
          Audit_personality.objects.filter(userid=member).update(audit_personality_R=audit_personality_R,
                                                                 audit_personality_I=audit_personality_I,
                                                                 audit_personality_A=audit_personality_A,
                                                                 audit_personality_S=audit_personality_S,
                                                                 audit_personality_E=audit_personality_E,
                                                                 audit_personality_C=audit_personality_C)


      else:
        Audit_personality.objects.create(userid=member,
                                         audit_personality_R=audit_personality_R,
                                         audit_personality_I=audit_personality_I,
                                         audit_personality_A=audit_personality_A,
                                         audit_personality_S=audit_personality_S,
                                         audit_personality_E=audit_personality_E,
                                         audit_personality_C=audit_personality_C)

      if  not Audit_career.objects.filter(audit_id=audit_id).exists():
        Audit_career.objects.create(audit_id=audit_id, userid=member, career_id=career)


    content_career = Career.objects.get(career_id=career_id)
    content_skill = Career_skill.objects.all().filter(career_id=career_id)


    return render(request, 'audit_skill.html', locals())
  else:
    return HttpResponseRedirect('/login/')


def audit_attitude(request):
  if request.session.has_key('userid'):
    audit_id = request.session['audit_id']
    audit = Audit_career.objects.get(audit_id=audit_id)
    userid = request.session['userid']
    member = Member.objects.get(userid=userid)
    career_id = request.GET['career_id']
    career = Career.objects.get(career_id=career_id)
    content_skill = Career_skill.objects.all().filter(career_id=career_id)


    if request.method == 'POST':
      skill = request.POST.getlist('skill')
      score = [request.POST['score_{}'.format(q)] for q in skill]

      print (len(skill))

    if Audit_skill.objects.filter(audit_id=audit_id).exists():
        audit_skill = Audit_skill.objects.filter(audit_id=audit_id)
        audit_skill.delete()

        i=0
        while i < len(skill):
          skill_id = skill[i]
          id = Career_skill.objects.get(skill_id=skill_id)
          audit_skill = Audit_skill()
          audit_skill.userid = member
          audit_skill.audit_id = audit
          audit_skill.skill_id = id
          audit_skill.score = score[i]
          # print(audit_skill.skill_id)
          audit_skill.save()
          i+=1

    else:
        i = 0
        while i < len(skill):
            # audit_skill_list = [audit, skill[i], score[i]]
            # print(audit_skill)
            skill_id = skill[i]
            id = Career_skill.objects.get(skill_id=skill_id)
            audit_skill = Audit_skill()
            audit_skill.userid = member
            audit_skill.audit_id = audit
            audit_skill.skill_id = id
            audit_skill.score = score[i]
            print(audit_skill.skill_id)
            audit_skill.save()
            i += 1

    content_career = Career.objects.get(career_id=career_id)
    content_attitude = Career_attitude.objects.all().filter(career_id=career_id)

    return render(request, 'audit_attitude.html', locals())
  else:
    return HttpResponseRedirect('/login/')


def audit_licence(request):
  if request.session.has_key('userid'):
    audit_id = request.session['audit_id']
    audit = Audit_career.objects.get(audit_id=audit_id)
    userid = request.session['userid']
    member = Member.objects.get(userid=userid)
    career_id = request.GET['career_id']
    career = Career.objects.get(career_id=career_id)
    content_skill = Career_skill.objects.all().filter(career_id=career_id)

    if request.method == 'POST':
      attitude = request.POST.getlist('attitude')
      score = [request.POST['score_{}'.format(q)] for q in attitude]

    if Audit_attitude.objects.filter(audit_id=audit_id).exists():
        audit_attitude = Audit_attitude.objects.filter(audit_id=audit_id)
        audit_attitude.delete()

        i = 0
        while i < len(attitude):
            attitude_id = attitude[i]
            id = Career_attitude.objects.get(attitude_id=attitude_id)
            audit_attitude = Audit_attitude()
            audit_attitude.userid = member
            audit_attitude.audit_id = audit
            audit_attitude.attitude_id = id
            audit_attitude.score = score[i]
            audit_attitude.save()
            i += 1

    else:
        i = 0
        while i < len(attitude):
            attitude_id = attitude[i]
            id = Career_attitude.objects.get(attitude_id=attitude_id)
            audit_attitude = Audit_attitude()
            audit_attitude.userid = member
            audit_attitude.audit_id = audit
            audit_attitude.attitude_id = id
            audit_attitude.score = score[i]
            # print(audit_skill.skill_id)
            audit_attitude.save()
            i += 1

    content_career = Career.objects.get(career_id=career_id)
    content_licence = Career_licence.objects.all().filter(career_id=career_id)

    return render(request, 'audit_licence.html', locals())
  else:
    return HttpResponseRedirect('/login/')


def audit_result(request):
  if request.session.has_key('userid'):
    audit_id = request.session['audit_id']
    audit = Audit_career.objects.get(audit_id=audit_id)
    userid = request.session['userid']
    member = Member.objects.get(userid=userid)
    career_id = request.GET['career_id']
    career = Career.objects.get(career_id=career_id)

    if request.method == 'POST':
        licence = request.POST.getlist('licence')
        score = [request.POST['score_{}'.format(q)] for q in licence]

    if Audit_attitude.objects.filter(audit_id=audit_id).exists():
        audit_licence = Audit_licence.objects.filter(audit_id=audit_id)
        audit_licence.delete()

        i = 0
        while i < len(licence):
            licence_id = licence[i]
            id = Career_licence.objects.get(licence_id=licence_id)
            audit_licence = Audit_licence()
            audit_licence.userid = member
            audit_licence.audit_id = audit
            audit_licence.licence_id = id
            audit_licence.score = score[i]
            audit_licence.save()
            i += 1

    else:
        i = 0
        while i < len(licence):
            licence_id = licence[i]
            id = Career_licence.objects.get(licence_id=licence_id)
            audit_licence = Audit_licence()
            audit_licence.userid = member
            audit_licence.audit_id = audit
            audit_licence.licence_id = id
            audit_licence.score = score[i]
            audit_licence.save()
            i += 1


#結果
    content_career = Career.objects.get(career_id=career_id)
    audit_id = request.session['audit_id']
    print(audit_id)
    audit = Audit_career.objects.get(audit_id=audit_id)

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


    return render(request, 'audit_result.html', locals())
  else:
    return HttpResponseRedirect('/login/')

