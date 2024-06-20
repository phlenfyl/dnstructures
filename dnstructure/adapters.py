from allauth.account.adapter import DefaultAccountAdapter
from django.forms import ValidationError

class CustomAccountAdapter(DefaultAccountAdapter):

    def clean_username(self, username, shallow=False):
        if username:
            raise ValidationError('Usernames are not allowed.')
        return username

    def save_user(self, request, user, form, commit=True):
        user = super().save_user(request, user, form, commit=False)
        user.email = form.cleaned_data.get('email')
        if 'password1' in form.cleaned_data:
            user.set_password(form.cleaned_data["password1"])
        else:
            user.set_unusable_password()
        if commit:
            user.save()
        return user