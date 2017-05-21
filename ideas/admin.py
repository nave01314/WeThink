from django.contrib import admin

from django.contrib import admin

from .models import Idea
from .models import IdeaTag

admin.site.register(Idea)
admin.site.register(IdeaTag)
