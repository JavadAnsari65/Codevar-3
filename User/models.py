from django.db import models
from ProjectGroupOrder.Tools import GetDifferenceTime , ValidationText
from django.db.models import Q
class Project(models.Model):
    User = models.ForeignKey('User.User',on_delete=models.CASCADE)
    Title = models.CharField(max_length=65)
    Technologies = models.CharField(max_length=100)
    DeadLineByUser = models.CharField(null=True,blank=True,max_length=100)
    DeadLineFinally = models.CharField(null=True,blank=True,max_length=100)
    BudgetByUser = models.CharField(null=True,blank=True,max_length=100)
    BudgetFinally = models.CharField(null=True,blank=True,max_length=100)
    Description = models.TextField()
    DescriptionAdmin = models.TextField(null=True,blank=True)
    DateSubmit = models.DateTimeField()
    StateProject = (
        ('Cancel','لغو'),
        ('Checking','در حال بررسی'),
        ('WaitPay','در انتظار پرداخت'),
        ('WorkingOn','در دست ساخت'),
        ('Ended','تمام شده'),
    )
    StateProject = models.CharField(choices=StateProject,max_length=10)

    def __str__(self):
        return self.User.__str__()

    def GetStateProject(self):
        return self.get_StateProject_display()

    def TimePastSubmit(self):
        return GetDifferenceTime(self.DateSubmit)


class User(models.Model):
    UserNameFamily = models.CharField(max_length=150,null=True,blank=True)
    PhoneNumber = models.CharField(max_length=20,null=True,blank=True)
    Email = models.CharField(max_length=100,null=True,blank=True)
    Address = models.TextField(null=True,blank=True)
    DateTimeJoin = models.DateTimeField()
    UserName = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)

    def __str__(self):
        return self.UserNameFamily or 'Ghost'

    def GetNameAndFamily(self):
        return self.UserNameFamily or 'User'

    def GerSrcPanel(self):
        return '/U/Profile'

    def GetTitleUserModel(self):
        return 'User'

    def InfoIsComplete(self):
        if ValidationText(self.UserNameFamily,3,150) and ValidationText(self.PhoneNumber,10,12) and ValidationText(self.Email,3,150):
            return True
        return False


    def ProjectChecking(self):
        LookUp = Q(StateProject='Checking') | Q(StateProject='WaitPay')
        Objects = Project.objects.filter(LookUp,User_id=self.id)
        return sorted(Objects , key=lambda Object : Object.StateProject == 'WaitPay')[::-1]


    def ProjectWorkingOn(self):
        return Project.objects.filter(User_id=self.id,StateProject='WorkingOn')[::-1]

    def ProjectEnded(self):
        return Project.objects.filter(User_id=self.id,StateProject='Ended')[::-1]






