from django import forms
from .models import Potoci, TelegramUser, Channel


class MultiSelectUserWidget(forms.SelectMultiple):
    def value_from_datadict(self, data, files, name):
        values = super().value_from_datadict(data, files, name)
        if isinstance(values, list):
            return values
        return values.split(',') if values else []
    
class PotociAdminForm(forms.ModelForm):
    user = forms.ModelMultipleChoiceField(
        queryset=TelegramUser.objects.all(),
        widget=MultiSelectUserWidget,
    )
    class Meta:
        model = Potoci
        fields = '__all__'
        widgets = {
            'user': MultiSelectUserWidget,
            'title': forms.TextInput
        }

class Telefram_UserForm(forms.ModelForm):

    class Meta: 
        models = TelegramUser
        fields = '__all__'
        widgets = {
            'name': forms.TextInput,
            'familia': forms.TextInput,
            'bio': forms.TextInput,
            'phone': forms.TextInput,
            'api_id': forms.TextInput,
            'api_hash': forms.TextInput
        }

#class ChanelForm(forms.ModelForm):
#    class Meta:
#        models = Channel
#        fields = '__all__'
#        widgets = {
#            'name_chanel': forms.TextInput,
#            'link_for_cahal': forms.TextInput
#        }



