from django.contrib import admin
from .models import Profile, Education, Experience, Publications, Operations, Specialization
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    pass

class EducationAdmin(admin.ModelAdmin):
    pass

class ExperienceAdmin(admin.ModelAdmin):
    pass

class PublicationsAdmin(admin.ModelAdmin):
    pass

class OperationsAdmin(admin.ModelAdmin):
    pass

class SpecializationAdmin(admin.ModelAdmin):
    pass

admin.site.register(Profile)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Publications)
admin.site.register(Operations)
admin.site.register(Specialization)