from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm


# Register your models here.

class GradChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Alumni

class GraduateAdmin(UserAdmin):
    form = GradChangeForm
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('summary','profile_picture','university', 'year_graduated')}),
    )


class ClubAdmin(admin.ModelAdmin):
    list_display = ('name',)


class UniAdmin(admin.ModelAdmin):
    list_display = ('name',)


class MessageAdmin(admin.ModelAdmin):
    list_display = ('chat_room','yazan','mesaj')


class ReplyAdmin(admin.ModelAdmin):
    list_display = ('chat_room','yazan','mesaj','main',)


admin.site.register(Alumni,GraduateAdmin)
admin.site.register(University,UniAdmin)
admin.site.register(Club,ClubAdmin)
admin.site.register(Message,MessageAdmin)
admin.site.register(ReplyMessage,ReplyAdmin)