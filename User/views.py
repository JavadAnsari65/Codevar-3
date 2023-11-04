import json

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from MemberGroup.models import MemberGroup
from ProjectGroupOrder.Security import Decode
from ProjectGroupOrder.Tools import GetTimeIran, SerializerTool
from ProjectGroupOrder.User import GetUser_ByMODEL
from .models import *


def Panel(request):
    Context = {}
    User = GetUser_ByMODEL(request, 'User')
    if User is None:
        return redirect('/U/Login-Create')
    Context['User'] = User
    Context['ProjectChecking'] = User.ProjectChecking() or None
    Context['ProjectWorkingOn'] = User.ProjectWorkingOn() or None
    Context['ProjectEnded'] = User.ProjectEnded() or None
    return render(request, 'panel.html', Context)


def LoginCreate(request):
    return render(request, 'Login-Create-User/index.html')


@csrf_exempt
def LoginCheck(request):
    Context = {}
    Data = json.loads(request.body)
    UserName = Data.get('UserName') or None
    Password = Data.get('Password') or None
    if (ValidationText(UserName, None, None, True, True)) and (ValidationText(Password, None, None, True, True)):
        StateUser = User.objects.filter(UserName=UserName, Password=Password).first()
        if StateUser is not None:
            Context['Status'] = '200'
            Context['QlYSqVS'] = Decode(UserName)
            Context['YPtIeRC'] = Decode(Password)
        else:
            Context['Status'] = '404'
    else:
        Context['Status'] = '204'
    return JsonResponse(Context)


@csrf_exempt
def CreateAccount(request):
    Context = {}
    Data = json.loads(request.body)
    UserName = Data.get('UserName') or None
    Email = Data.get('Email') or None
    Password = Data.get('Password') or None
    if (ValidationText(UserName, 4, 65, True, True) and ValidationText(Email, 0, 100) and ValidationText(Password, 7,
                                                                                                         100, True,
                                                                                                         True)):
        UserExists = User.objects.filter(UserName=UserName).first() or MemberGroup.objects.filter(
            UserName=UserName).first()
        if UserExists == None:
            User.objects.create(UserName=UserName, Password=Password, Email=Email, DateTimeJoin=GetTimeIran())
            Context['Status'] = '200'
            Context['QlYSqVS'] = Decode(UserName)
            Context['YPtIeRC'] = Decode(Password)
        else:
            Context['Status'] = '409'
    else:
        Context['Status'] = '204'

    return JsonResponse(Context)


@csrf_exempt
def SubmitProject(request):
    Context = {}
    Data = json.loads(request.body)
    User = GetUser_ByMODEL(request, 'User')
    if User is not None:
        TitleProject = Data.get('TitleProject') or None
        Technologies = Data.get('Technologies') or None
        DeadLine = Data.get('DeadLine') or None
        Budget = Data.get('Budget') or None
        Description = Data.get('Description') or None
        if ValidationText(TitleProject, 4, 65) and ValidationText(Technologies, 4, 100) and ValidationText(DeadLine, 0,
                                                                                                           5) and ValidationText(
                Budget, 2, 50) and ValidationText(Description, 1, 5000):
            if User.InfoIsComplete():
                Project.objects.create(User_id=User.id, Title=TitleProject, Technologies=Technologies,
                                       DeadLineByUser=DeadLine, BudgetByUser=Budget, Description=Description,
                                       DateSubmit=GetTimeIran(), StateProject='Checking')
                Context['Status'] = '200'
            else:
                Context['Status'] = '205'
        else:
            Context['Status'] = '204'
    else:
        Context['__Redirect__'] = 'True'
        Context['__RedirectURL__'] = '/'
    return JsonResponse(Context)


@csrf_exempt
def CancelProject(request):
    Context = {}
    Data = json.loads(request.body)
    ID = Data.get('ID') or None
    User = GetUser_ByMODEL(request, 'User') or None
    if User is not None:
        if ValidationText(ID):
            ProjectExists = Project.objects.filter(id=ID, User_id=User.id).first()
            if ProjectExists is not None:
                ProjectExists.StateProject = 'Cancel'
                ProjectExists.save()
                Context['Status'] = '200'
            else:
                Context['Status'] = '404'
        else:
            Context['Status'] = '204'
    else:
        Context['__Redirect__'] = 'True'
        Context['__RedirectURL__'] = '/'

    return JsonResponse(Context)


@csrf_exempt
def SubmitInfo(request):
    Context = {}
    Data = json.loads(request.body)
    User = GetUser_ByMODEL(request, 'User')
    if User is not None:
        UserNameAndFamily = Data.get('UserNameAndFamily') or None
        PhoneNumber = Data.get('PhoneNumber') or None
        Email = Data.get('Email') or None
        Address = Data.get('Address') or None
        if ValidationText(UserNameAndFamily, 3, 150) and ValidationText(PhoneNumber, 10, 12) and ValidationText(Email,
                                                                                                                3, 150):
            User.UserNameFamily = UserNameAndFamily
            User.PhoneNumber = PhoneNumber
            User.Email = Email
            User.Address = Address
            User.save()
            Context['Status'] = '200'
        else:
            Context['Status'] = '204'
    else:
        Context['__Redirect__'] = 'True'
        Context['__RedirectURL__'] = '/U/Login-Create'
    return JsonResponse(Context)


@csrf_exempt
def GetProject(request):
    Context = {}
    Data = json.loads(request.body)
    ID = Data.get('ID') or None
    User = GetUser_ByMODEL(request, 'User')
    if User is not None:
        if ValidationText(ID):
            ProjectExists = Project.objects.filter(User_id=User.id, id=ID).first()
            if ProjectExists is not None:
                Object = {}
                # Object['ID'] = ProjectExists.id
                # Object['Title'] = ProjectExists.Title
                # Object['TimePastSubmit'] = ProjectExists.TimePastSubmit()
                # Object['Technologies'] = ProjectExists.Technologies
                # Object['DeadLineByUser'] = ProjectExists.DeadLineByUser
                # Object['DeadLineFinally'] = ProjectExists.DeadLineFinally
                # Object['BudgetByUser'] = ProjectExists.BudgetByUser
                # Object['BudgetFinally'] = ProjectExists.BudgetFinally
                # Object['Description'] = ProjectExists.Description
                # Object['DescriptionAdmin'] = ProjectExists.DescriptionAdmin
                # Object['DateSubmit'] = ProjectExists.DateSubmit
                # Object['StateProject'] = ProjectExists.StateProject
                # Object['StateProjectTitle'] = ProjectExists.GetStateProject()
                Context['Object'] = \
                SerializerTool(Project, [ProjectExists], '__All__', ['TimePastSubmit', 'GetStateProject'])[0] or None
                Context['Status'] = '200'
            else:
                Context['Status'] = '204'
        else:
            Context['Status'] = '204'
    else:
        Context['__Redirect__'] = 'True'
        Context['__RedirectURL__'] = '/U/Login-Create'

    return JsonResponse(Context)
