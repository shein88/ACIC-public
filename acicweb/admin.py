from django.contrib.admin import AdminSite

from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(VisObjCon)
admin.site.register(BoardOfDirectors)
admin.site.register(Team)
admin.site.register(Collabrations)
admin.site.register(StartUps)
admin.site.register(Mentors)
admin.site.register(MakersLab)
admin.site.register(Events)
admin.site.register(EventNames)
admin.site.register(EventDetails)
admin.site.register(SectorSpecificLab)
admin.site.register(CommunityInnovativeSpace)
