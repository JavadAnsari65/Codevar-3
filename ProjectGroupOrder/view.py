from django.shortcuts import render

from .User import GetUser_ByMODEL


def Home(request):
    ##
    return render(request, 'Home/index.html')


def Handler_Err_404(request, exception=None):
    Context = {}
    User = GetUser_ByMODEL(request, 'User')
    Member = GetUser_ByMODEL(request, 'MemberGroup')
    Context['User_Member'] = User or Member
    return render(request, 'Components/ErrorsPage/404.html', Context)


handler404 = Handler_Err_404
