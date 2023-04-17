from django.contrib import admin
from .models import Questions
# Register your models here.

class QuestionsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Questions)