from django.contrib import admin
from .models import User, Exercise_Category, Tag
from GX.models import Conference, User_Conference
from trainer.models import Request_Counsel, Member_Coach, Counsel
from PX.models import Diet, Training_History, Schedule
from profiles.models import Weight
from community.models import Article, Comment

admin.site.register(User)
admin.site.register(Exercise_Category)
admin.site.register(Tag)

admin.site.register(Conference)
admin.site.register(User_Conference)

admin.site.register(Request_Counsel)
admin.site.register(Member_Coach)
admin.site.register(Counsel)

admin.site.register(Diet)
admin.site.register(Training_History)
admin.site.register(Schedule)

admin.site.register(Weight)

admin.site.register(Article)
admin.site.register(Comment)
