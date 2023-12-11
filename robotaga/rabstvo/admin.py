from django.contrib import admin
from django import forms
from .models import TelegramUser, Channel, Potoci, Api_tocken
from .forms import PotociAdminForm, Telefram_UserForm#, ChanelForm


# Register your models here.

class ChannelAdmin(admin.StackedInline):
    model = Channel
    extra = 0
#    form = ChanelForm

@admin.register(TelegramUser)
class PostAdmin(admin.ModelAdmin):
    inlines = [ChannelAdmin]
    

    class Meta:
       model = TelegramUser
        
    def get_channels(self, obj):
        return ", ".join([channel.name_chanel for channel in obj.channel_set.all()])

    get_channels.short_description = 'Channels'
    list_display = ('name', 'familia','bio','get_channels')
    search_fields = ['name', 'channel__name_chanel']
    form = Telefram_UserForm




class ClassPotoci(admin.ModelAdmin):
    list_display = ('get_user', 'title_', 'text')
    search_fields = ['user__name', 'title']
    list_editable = ['text']
    form = PotociAdminForm
    list_per_page = 5

    def title_(self, obj):
        return forms.TextInput().render('title',obj.title)
    def get_user(self, obj):
        return ','.join([u.name for u in obj.user.all()]) 


admin.site.register(Potoci, ClassPotoci)

admin.site.register(Api_tocken)
