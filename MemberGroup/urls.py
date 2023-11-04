from django.urls import path

from .views import *

app_name = 'MemberGroup'
urlpatterns = [
    path('Profile', Panel),
    path('Profile/Submit/Info', SubmitInfo),
    path('Login-Create', LoginCreateAccount, name='Login-Create'),
    path('Login/LoginCheck', LoginCheck),
    path('CreateAccount', CreateAccount),
    path('Profile/Skill/Add', AddSkill),
    path('Profile/Skill/Remove', RemoveSkill),
    path('Profile/WorkSample/Add', AddWorkSample),
    path('Profile/WorkSample/Remove', RemoveWorkSample),
    path('Profile/WorkSample/Get', GetWorkSample),
    path('Profile/WorkSample/Edit', EditWorkSample),
    path('WorkSample/LikeDisLike', LikeDisLikeWorkSample),
    path('LikeDisLikeMember', LikeDisLikeMember),
    path('<ID>/Profile', ShowProfileMember),
]
