from django.db import models
from ProjectGroupOrder.Tools import GetDifferenceTime, GetDifferenceTimeObj
import random, string


def RandomString(Len):
    Letters = string.ascii_lowercase
    return ''.join(random.choice(Letters) for i in range(Len))


def UploadSrcImageInfo(instance, path):
    Format = str(path).split('.')[1]
    return f'Images/Members/{instance.id}/Profile/{RandomString(random.randint(4, 15))}.{Format}'


def UploadSrcImageWorkSample(instance, path):
    Format = str(path).split('.')[1]
    return f'Images/Members/{instance.id}/Profile/WorkSamples/{RandomString(random.randint(6, 15))}.{Format}'


class LikeWorkSample(models.Model):
    Owner = models.ForeignKey('User.User', on_delete=models.CASCADE)
    WorkSample = models.ForeignKey('MemberGroup.WorkSample', on_delete=models.CASCADE)

    def __str__(self):
        return self.Owner.UserNameFamily or 'Unknwon'


class LikeMember(models.Model):
    Owner = models.ForeignKey('User.User', on_delete=models.CASCADE)
    Member = models.ForeignKey('MemberGroup.MemberGroup', on_delete=models.CASCADE)

    def __str__(self):
        return self.Member.GetNameAndFamily() or 'Unknwon'


class Skill(models.Model):
    Owner = models.ForeignKey('MemberGroup.MemberGroup', on_delete=models.CASCADE)
    Title = models.CharField(max_length=100)
    ValueSkill = models.IntegerField()
    Description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.Title

    def Remove(self):
        self.delete()


class WorkSample(models.Model):
    Owner = models.ForeignKey('MemberGroup.MemberGroup', on_delete=models.CASCADE)
    Title = models.CharField(max_length=100)
    Address = models.CharField(max_length=150)
    TimeElapsed = models.CharField(max_length=20)
    Technologies = models.CharField(max_length=300)
    Description = models.TextField()
    Image = models.ImageField(upload_to=UploadSrcImageWorkSample)
    DateCreate = models.DateTimeField()

    def __str__(self):
        return self.Title

    def Remove(self):
        self.delete()

    def GetTimePastCreate(self):
        return GetDifferenceTime(self.DateCreate)

    def GetLikes(self):
        return LikeWorkSample.objects.filter(WorkSample_id=self.id)

    def GetLenLikes(self):
        return self.GetLikes().count()

    def GetCoverImage(self):
        return self.Image.url

    def ListIDUserLiked(self):
        return [O.id for O in [I.Owner for I in LikeWorkSample.objects.filter(WorkSample_id=self.id)]]


class MemberGroup(models.Model):
    UserNameFamily = models.CharField(max_length=150, null=True, blank=True)
    PhoneNumber = models.CharField(max_length=30, null=True, blank=True)
    Phone = models.CharField(max_length=30, null=True, blank=True)
    Email = models.CharField(max_length=100, null=True, blank=True)
    NationalCode = models.CharField(max_length=30, null=True, blank=True)
    TitleJob = models.CharField(max_length=300, null=True, blank=True)
    Address = models.TextField(null=True, blank=True)
    Github = models.CharField(max_length=300,null=True,blank=True)
    AboutMe = models.TextField(null=True, blank=True)
    Image = models.ImageField(null=True, blank=True, upload_to=UploadSrcImageInfo)
    UserActive = models.BooleanField(default=True)
    DateTimeJoin = models.DateTimeField()
    UserName = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    Is_Active = models.BooleanField(default=False)

    def __str__(self):
        return self.UserNameFamily or 'User'

    def GetNameAndFamily(self):
        return self.UserNameFamily or 'User'

    def SubmitAndUpdateInfo(self, UserNameFamily, PhoneNumber, Phone, Email, NationalCode, TitleJob, Github, Address,
                            AboutMe, Image=None):
        self.UserNameFamily = UserNameFamily
        self.PhoneNumber = PhoneNumber
        self.Phone = Phone
        self.Email = Email
        self.NationalCode = NationalCode
        self.TitleJob = TitleJob
        self.Github = Github
        self.Address = Address
        self.AboutMe = AboutMe
        if Image is not None:
            self.Image = Image
        self.save()

    def GetTimeJoined(self):
        return GetDifferenceTime(self.DateTimeJoin)

    def StateInfo(self):
        if (
                (self.UserNameFamily is not '' and self.UserNameFamily is not None) and
                (self.PhoneNumber is not '' and self.PhoneNumber is not None) and
                (self.Phone is not '' and self.Phone is not None) and
                (self.Email is not '' and self.Email is not None) and
                (self.NationalCode is not '' and self.NationalCode is not None) and
                (self.TitleJob is not '' and self.TitleJob is not None) and
                (self.Address is not '' and self.Address is not None) and
                (self.Image is not '' and self.Image is not None)
        ):
            return True
        else:
            return False

    def GetSkills(self):
        return Skill.objects.filter(Owner_id=self.id)[::-1]

    def GetSkillsWithValue(self):
        Skills = Skill.objects.filter(Owner_id=self.id) or []
        return [j for j in [{"Value": i.ValueSkill, "Title": i.Title} for i in Skills]]

    def GetLenSkills(self):
        return len(Skill.objects.filter(Owner_id=self.id)) or 0

    def GetWorkSamples(self):
        return WorkSample.objects.filter(Owner_id=self.id)[::-1]

    def GetLenWorkSamples(self):
        return len(WorkSample.objects.filter(Owner_id=self.id)) or 0

    def GerSrcPanel(self):
        return '/M/Profile'

    def GetLenLikeMember(self):
        return len(LikeMember.objects.filter(Member_id=self.id))

    def GetListIDUsersLiked(self):
        return [i.Owner.id for i in LikeMember.objects.filter(Member_id=self.id)]

    def GetLevelStatus(self):
        LenWorkSamples = self.GetLenWorkSamples()
        DaysJoined = int(GetDifferenceTimeObj(self.DateTimeJoin).get('Day'))
        Text = 'تازه وارد'
        if LenWorkSamples > 2 and DaysJoined > 20:
            Text = 'نیمه وارد'
        if LenWorkSamples > 4 and DaysJoined > 35:
            Text = 'وارد'
        if LenWorkSamples > 7 and DaysJoined > 50:
            Text = 'کهنه کار'

        return Text

    def GetTitleUserModel(self):
        return 'Member'
