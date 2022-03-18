from django.contrib import admin
from .models import *
admin.site.register(MemberGroup)
admin.site.register(Skill)
admin.site.register(WorkSample)
admin.site.register(LikeWorkSample)
admin.site.register(LikeMember)