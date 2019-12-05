from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile
from django.utils.safestring import mark_safe


class ProfileAdmin(admin.ModelAdmin):
		# pass
		list_display = ['user', 'funcao', 'image_tag']
		# readonly_fields = ('image_tag',)

admin.site.register(Profile, ProfileAdmin)



