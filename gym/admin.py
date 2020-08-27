from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from gym.models import Message, Profile, Exercise

# Register your models here.

# ---------- this code id admin side----------


class MessageAdmin(ModelAdmin):
    list_display = ["subject", "cr_date"]  # link show name
    search_fields = ['subject', 'msg']     # search bar
    list_filter = ['cr_date']              # filter bar


admin.site.register(Message, MessageAdmin)  # compelsory


class ProfileAdmin(ModelAdmin):
    list_display = ["name"]
    search_fields = ["name", "status", "phone_no"]
    list_filter = ["status", "gender"]


admin.site.register(Profile, ProfileAdmin)


admin.site.register(Exercise)
