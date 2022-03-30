from django.shortcuts import render, redirect
from .User import GetUser_ByMODEL
from MemberGroup.models import WorkSample, MemberGroup


def Home(request):
    Context = {}
    User = GetUser_ByMODEL(request, 'User')
    Member = GetUser_ByMODEL(request, 'MemberGroup')
    Context['OnlyUserIsLogin'] = True if User is not None else False
    Context['User'] = User
    Context['Member'] = Member
    Context['User_Member'] = User or Member
    Context['WorkSamples'] = WorkSample.objects.filter(Owner__Is_Active=True)[::-1][:2]
    Context['Members'] = MemberGroup.objects.filter(Is_Active=True)[::-1][:3]
    return render(request, 'Home/index.html', Context)


def WorkSamples(request):
    Context = {}
    User = GetUser_ByMODEL(request, 'User')
    Member = GetUser_ByMODEL(request, 'MemberGroup')
    Context['OnlyUserIsLogin'] = True if User is not None else False
    Context['User'] = User
    Context['Member'] = Member
    Context['User_Member'] = User or Member
    Context['WorkSamples'] = WorkSample.objects.filter(Owner__Is_Active=True)[::-1]
    return render(request, 'WorkSample/index.html', Context)


def Members(request):
    Context = {}
    User = GetUser_ByMODEL(request, 'User')
    Member = GetUser_ByMODEL(request, 'MemberGroup')
    Context['OnlyUserIsLogin'] = True if User is not None else False
    Context['User'] = User
    Context['Member'] = Member
    Context['User_Member'] = User or Member
    Context['Members'] = sorted(MemberGroup.objects.filter(Is_Active=True), key=lambda O: O.GetLenLikeMember())[::-1]
    return render(request, 'Members/index.html', Context)


#   Errors


def Handler_Err_404(request,exception=None):
    Context = {}
    User = GetUser_ByMODEL(request, 'User')
    Member = GetUser_ByMODEL(request, 'MemberGroup')
    Context['User_Member'] = User or Member
    return render(request, 'Components/ErrorsPage/404.html',Context)

handler404  = Handler_Err_404
