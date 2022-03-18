import json

from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from ProjectGroupOrder.Tools import GetTimeIran, ValidationText, ValidationNumber
from MemberGroup.models import *
from ProjectGroupOrder.Security import Decode
from ProjectGroupOrder.User import GetUser_ByMODEL, GetUser
from ProjectGroupOrder.Tools import Set_Cookie, Set_Cookie_Functionality
from User.models import User


def Panel(request):
    Context = {}
    User = GetUser_ByMODEL(request, 'MemberGroup')
    if User == None:
        return redirect('/M/Login-Create')
    Context['User'] = User
    Context['Member'] = User
    return render(request, 'index.html', Context)


def SubmitInfo(request):
    if request.POST:
        Data = request.POST
        User = GetUser_ByMODEL(request, 'MemberGroup')
        UserNameFamily = Data.get('UserNameFamily') or None
        PhoneNumber = Data.get('PhoneNumber') or None
        Phone = Data.get('Phone') or None
        Email = Data.get('Email') or None
        NationalCode = Data.get('NationalCode') or None
        TitleJob = Data.get('TitleJob') or None
        Address = Data.get('Address') or None
        AboutMe = Data.get('AboutMe') or None
        Image = request.FILES.get('Image') or None
        ImageState = Data.get('ImageState')
        if User is not None:
            if User.UserActive == True:
                if ((UserNameFamily is not None) and
                        (PhoneNumber is not None) and
                        (Phone is not None) and
                        (Email is not None) and
                        (NationalCode is not None) and
                        (TitleJob is not None) and
                        (Address is not None) and
                        (AboutMe is not None)):
                    if ImageState == 'MostGet':
                        if Image is not None:
                            User.SubmitAndUpdateInfo(UserNameFamily, PhoneNumber, Phone, Email, NationalCode, TitleJob,
                                                     Address, AboutMe, Image)
                            return Set_Cookie_Functionality(" اطلاعات شما با موفقیت ذخیره شدند ", 'Success', '7000',
                                                            '3', '/M/Profile?Info')
                        else:
                    
                            return Set_Cookie_Functionality("مشکلی در دریافت عکس وجود دارد ", 'Error', '7000',
                                                            '3', '/M/Profile?Info')
                    else:
                        User.SubmitAndUpdateInfo(UserNameFamily, PhoneNumber, Phone, Email, NationalCode, TitleJob,
                                                 Address, AboutMe)
                        return Set_Cookie_Functionality(" اطلاعات شما با موفقیت ذخیره شدند ", 'Success', '7000', '3',
                                                        '/M/Profile?Info')
                else:
                    return Set_Cookie_Functionality(" خطا : لطفا مجددا مقادیر را پر نمایید ", 'Error', '7000', '3',
                                                    '/M/Profile?Info')
            else:
                return Set_Cookie_Functionality("  حساب شما فعال نیست ", 'Error', '7000', '3',
                                                '/M/Profile?Info')
        return Set_Cookie_Functionality(" شما دسترسی ندارید ", 'Error', '7000', '3', '/M/Profile?Info')
    return redirect('/')


#                               Note
# Set_Cookie_Functionality ->>> Set Cookie And Redirect To Previous  Page

def LoginCreateAccount(request):
    User = GetUser_ByMODEL(request, 'MemberGroup')
    if User != None:
        return redirect('/M/Profile')
    return render(request, 'Login-Create/index.html')


@csrf_exempt
def LoginCheck(request):
    Context = {}
    Data = json.loads(request.body)
    UserName = Data.get('UserName') or None
    Password = Data.get('Password') or None
    if (ValidationText(UserName,None,None,True,True)) and (ValidationText(Password,None,None,True,True)):
        StateUser = MemberGroup.objects.filter(UserName=UserName, Password=Password).first()
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
    if (ValidationText(UserName, 4, 65,True,True) and ValidationText(Email, 0, 100) and ValidationText(Password, 7, 100,True,True)):
        UserExists = MemberGroup.objects.filter(UserName=UserName).first() or User.objects.filter(UserName=UserName).first()
        if UserExists == None:
            Context['QlYSqVS'] = Decode(UserName)
            Context['YPtIeRC'] = Decode(Password)
            MemberGroup.objects.create(UserName=UserName, Password=Password, Email=Email, DateTimeJoin=GetTimeIran())
            Context['Status'] = '200'
        else:
            Context['Status'] = '409'
    else:
        Context['Status'] = '204'

    return JsonResponse(Context)


@csrf_exempt
def AddSkill(request):
    Context = {}
    Data = json.loads(request.body)
    TitleSkill = Data.get('TitleSkill') or None
    ValueSkill = Data.get('ValueSkill') or None
    DescriptionSkill = Data.get('DescriptionSkill') or None
    User = GetUser_ByMODEL(request, 'MemberGroup')
    if (ValidationText(TitleSkill) and ValidationNumber(ValueSkill) and User is not None):
        SkillCreated = Skill.objects.create(Owner=User, Title=TitleSkill, ValueSkill=ValueSkill,
                                            Description=DescriptionSkill)
        Context['Status'] = '200'
        Context['IDSkill'] = SkillCreated.id
    else:
        Context['Status'] = '403'
    return JsonResponse(Context)


@csrf_exempt
def RemoveSkill(request):
    Context = {}
    Data = json.loads(request.body)
    ID = Data.get('ID') or None
    User = GetUser_ByMODEL(request, 'MemberGroup')
    if User is not None:
        StateSkill = Skill.objects.filter(id=ID).first()
        if StateSkill is not None:
            StateSkill.delete()
            Context['Status'] = '200'
        else:
            Context['Status'] = '404'
    else:
        Context['Status'] = '403'
    return JsonResponse(Context)


@csrf_exempt
def AddWorkSample(request):
    User = GetUser_ByMODEL(request, 'MemberGroup')
    Data = request.POST
    Title = Data.get('Title') or None
    AddressWorkSample = Data.get('AddressWorkSample') or None
    TimeElapsed = Data.get('TimeElapsed') or None
    Technologies = Data.get('Technologies') or None
    Description = Data.get('Description') or None
    Image = request.FILES.get('Image') or None
    if User is not None:
        if ValidationText(Title, 0, 100) and ValidationText(AddressWorkSample, 0, 150) and ValidationText(TimeElapsed,
                                                                                                          0,
                                                                                                          20) and ValidationText(
            Technologies, 0, 300) and ValidationText(Description, 0, 1000) and Image is not None:
            WorkSampleCreated = WorkSample.objects.create(Owner=User, Title=Title, Address=AddressWorkSample,
                                                          TimeElapsed=TimeElapsed, Technologies=Technologies,
                                                          Description=Description, Image=Image,
                                                          DateCreate=GetTimeIran())
            return Set_Cookie_Functionality("نمونه کار شما با موفقیت ساخته شد ", 'Success', '7000', '2',
                                            '/M/Profile?WorkSamples')
        else:
            return Set_Cookie_Functionality("لطفا تمامی فیلد هارا پر نمایید", 'Error', '7000', '2',
                                            '/M/Profile?WorkSamples')
    else:
        return Set_Cookie_Functionality("شما دسترسی ندارید", 'Error', '7000', '2', '/M/Profile?WorkSamples')


@csrf_exempt
def GetWorkSample(request):
    Context = {}
    Data = json.loads(request.body)
    ID = Data.get('ID') or None
    if ValidationText(ID):
        WorkSampleGet = WorkSample.objects.filter(id=ID).first()
        User = GetUser_ByMODEL(request, 'User')
        if WorkSampleGet is not None :
            Context['Status'] = '200'
            # Data = serializers.serialize('json',[WorkSampleGet])
            # Data = json.loads(Data)
            # Context['WorkSample'] = Data
            Data = {
                'ID': WorkSampleGet.id,
                'Title': WorkSampleGet.Title,
                'Description': WorkSampleGet.Description,
                'Address': WorkSampleGet.Address,
                'TimeElapsed': WorkSampleGet.TimeElapsed,
                'Technologies': WorkSampleGet.Technologies,
                'TimePast': WorkSampleGet.GetTimePastCreate(),
                'ImageUrl': WorkSampleGet.Image.url,
                'UserNameCreator': WorkSampleGet.Owner.UserNameFamily,
                'ID_UserNameCreator': WorkSampleGet.Owner.id,
                'Likes': len(WorkSampleGet.GetLikes())
            }
            if User is not None:
                Data['StateRequest'] = 'User'
                Data['Liked'] = 'true' if LikeWorkSample.objects.filter(Owner_id=User.id,WorkSample_id=WorkSampleGet.id).first() != None else 'false'
            else:
                Data['StateRequest'] = 'Unknown'
                Data['Liked'] = 'false'

            Context['Object'] = Data
        else:
            Context['Status'] = '409'
    return JsonResponse(Context)


@csrf_exempt
def RemoveWorkSample(request):
    Context = {}
    Member = GetUser_ByMODEL(request, 'MemberGroup')
    if Member is not None:
        Data = json.loads(request.body)
        ID = Data.get('ID') or None
        if ID is not None and ID is not '':
            WorkSample.objects.filter(id=ID).first().Remove()
            Context['Status'] = '200'
        else:
            Context['Status'] = '409'
    else:
        Context['Status'] = '403'
    return JsonResponse(Context)


@csrf_exempt
def LikeDisLikeWorkSample(request):
    Context = {}
    Data = json.loads(request.body)
    ID = Data.get('ID') or None
    State = Data.get('State') or None
    User = GetUser_ByMODEL(request, 'User')
    if User is not None:
        if ValidationText(ID) and ValidationText(State):
            if State == 'true':
                # Dis Like
                LikeGet = LikeWorkSample.objects.filter(WorkSample_id=ID, Owner_id=User.id).first()
                if LikeGet is not None:
                    LikeGet.delete()
                    Context['Status'] = '200'
                else:
                    Context['Status'] = '404'
            elif State == 'false':
                # Like
                WorkSampleGet = WorkSample.objects.filter(id=ID).first()
                if WorkSampleGet is not None:
                    LikeCreate = LikeWorkSample.objects.create(Owner_id=User.id, WorkSample_id=WorkSampleGet.id)
                    Context['Status'] = '200'
                else:
                    Context['Status'] = '404'
        else:
            Context['Status'] = '409'
    else:
        Context['Status'] = '403'
    return JsonResponse(Context)


@csrf_exempt
def EditWorkSample(request):
    Context = {}
    Data = request.POST
    User = GetUser_ByMODEL(request,'MemberGroup')
    ID_Sample = Data.get('ID_Sample') or None
    Title = Data.get('Title') or None
    Address = Data.get('AddressWorkSample') or None
    TimeElapsed = Data.get('TimeElapsed') or None
    Technologies = Data.get('Technologies') or None
    Description = Data.get('Description') or None
    StateGetImage = Data.get('StateGetImage') or None
    Image = request.FILES.get('Image')

    def UpdateWorkSample(Object, Title, Address, TimeElapsed, Technologies, Description, Image=None):
        Object.Title = Title
        Object.Address = Address
        Object.TimeElapsed = TimeElapsed
        Object.Technologies = Technologies
        Object.Description = Description
        if Image is not None:
            Object.Image = Image
        Object.save()

    if ValidationText(ID_Sample) and ValidationText(Title, 0, 100) and ValidationText(Address, 0,
                                                                                      150) and ValidationText(
            TimeElapsed, 0, 20) and ValidationText(Technologies, 0, 300) and ValidationText(Description, 0, 1000) and User is not None:
        StateSampleGet = WorkSample.objects.filter(id=ID_Sample,Owner_id=User.id).first()
        if StateSampleGet is not None:
            if Image is not None:
                UpdateWorkSample(StateSampleGet, Title, Address, TimeElapsed, Technologies, Description, Image)
                return Set_Cookie_Functionality("اطلاعات نمونه کار شما با موفقیت تغییر کردند", 'Success',
                                                RedirectTo='/M/Profile?WorkSamples')
            else:
                if StateGetImage == 'MostGet':
                    return Set_Cookie_Functionality("خطا | لطفا فیلد عکس را به درستی پر نمایید", 'Error',
                                                    RedirectTo='/M/Profile?WorkSamples')
                else:
                    UpdateWorkSample(StateSampleGet, Title, Address, TimeElapsed, Technologies, Description, None)
                    return Set_Cookie_Functionality("اطلاعات نمونه کار شما با موفقیت تغییر کردند", 'Success',
                                                    RedirectTo='/M/Profile?WorkSamples')
        else:
            return Set_Cookie_Functionality("خطا | لطفا مجددا تلاش کنید ", 'Error', RedirectTo='/M/Profile?WorkSamples')
    else:
        return Set_Cookie_Functionality("خطا | لطفا فیلد هارا پر نمایید ", 'Error', RedirectTo='/M/Profile?WorkSamples')
    # For ensure
    return HttpResponse('')


@csrf_exempt
def LikeDisLikeMember(request):
    Context = {}
    Data = json.loads(request.body)
    ID = Data.get('ID') or None
    if ValidationText(ID):
        User = GetUser_ByMODEL(request, 'User')
        Member = MemberGroup.objects.filter(id=int(ID)).first()
        if User is not None and Member is not None:
            StateLike = LikeMember.objects.filter(Owner_id=User.id, Member_id=Member.id).first()
            if StateLike is None:
                LikeMember.objects.create(Owner_id=User.id, Member_id=Member.id)
                Context['Status'] = '200'
            else:
                StateLike.delete()
                Context['Status'] = '204'
        else:
            Context['Status'] = '404'
    else:
        Context['Status'] = '403'
    return JsonResponse(Context)


def ShowProfileMember(request, ID):
    if ID.isdigit():
        Context = {}
        MemberProfile = MemberGroup.objects.filter(id=ID).first()
        if MemberProfile != None:
            User = GetUser_ByMODEL(request, 'User')
            Member = GetUser_ByMODEL(request, 'MemberGroup')
            Context['OnlyUserIsLogin'] = True if User is not None else False
            Context['ViewBy'] = 'User'
            Context['User'] = User
            Context['User_Member'] = User or Member
            Context['Member'] = Member
            Context['MemberProfile'] = MemberProfile
            return render(request, 'index-profile.html', Context)
    return redirect('/')
