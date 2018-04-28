# accounts.forms.py
from django import forms
from django.forms import TextInput
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User

#
# class ReisterForm(forms.Form):
#     name     = forms.CharField(widget=forms.TextInput(attrs={"autocomplete":"off" ,
#                                                         "type":"text" ,
#                                                          "name" :"log_username" ,
#                                                            "class":"required form-control"  ,
#                                                            "placeholder":"Username",
#                                                             "style":" margin-bottom: 10px;"}) , label='')
#
#     password = forms.CharField(widget=forms.PasswordInput(attrs={"autocomplete":"off" ,
#                                                         "type":"password" ,
#                                                          "name" :"log_password" ,
#                                                          "class":"password required form-control"  ,
#                                                          "placeholder":"Password" ,
#                                                          "style":" margin-bottom: 19px;"}) , label='')
#
#     password2 = forms.CharField(widget=forms.PasswordInput(attrs={"autocomplete":"off" ,
#                                                         "type":"password" ,
#                                                          "name" :"log_password2" ,
#                                                          "class":"password required form-control"  ,
#                                                          "placeholder":"Confirm password" ,
#                                                          "style":" margin-bottom: 19px;"}) , label='')
#
#     email     = forms.EmailField(widget=forms.TextInput(attrs={"autocomplete":"off" ,
#                                                         "type":"text" ,
#                                                          "name" :"email" ,
#                                                            "class":"required form-control"  ,
#                                                            "placeholder":"email",
#                                                             "style":" margin-bottom: 10px;"}) , label='')
#
#     fistName     = forms.CharField(widget=forms.TextInput(attrs={"autocomplete":"off" ,
#                                                         "type":"text" ,
#                                                          "name" :"firstName" ,
#                                                            "class":"required form-control"  ,
#                                                            "placeholder":"First name",
#                                                             "style":" margin-bottom: 10px;"}) , label='')
#
#     lastName     = forms.CharField(widget=forms.TextInput(attrs={"autocomplete":"off" ,
#                                                         "type":"text" ,
#                                                          "name" :"lastName" ,
#                                                            "class":"required form-control"  ,
#                                                            "placeholder":"Last name",
#                                                             "style":" margin-bottom: 10px;"}) , label='')

# class RegisterForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
#
#     class Meta:
#         model = User
#         fields = ('email',)
#
#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#         qs = User.objects.filter(email=email)
#         if qs.exists():
#             raise forms.ValidationError("email is taken")
#         return email
    #
    # def clean_password2(self):
    #     # Check that the two password entries match
    #     password1 = self.cleaned_data.get("password1")
    #     password2 = self.cleaned_data.get("password2")
    #     if password1 and password2 and password1 != password2:
    #         raise forms.ValidationError("Passwords don't match")
    #     return password2


class UserAdminCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email','user_name')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email','user_name', 'password', 'active', 'admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]




class RegisterForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={"autocomplete":"off" ,
                                                        "type":"password" ,
                                                         "name" :"log_password" ,
                                                         "class":"password required form-control"  ,
                                                         "placeholder":"Password" ,
                                                         "style":" margin-bottom: 19px;"}))

    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={"autocomplete":"off" ,
                                                        "type":"password" ,
                                                         "name" :"log_password" ,
                                                         "class":"password required form-control"  ,
                                                         "placeholder":"Password confirmation" ,
                                                         "style":" margin-bottom: 19px;"}) )

    class Meta:
        model = User
        fields = ('email','user_name')
        widgets = {
            'email': TextInput(attrs={"type":"text" ,"name" :"log_username" , "class":"required form-control"  , "placeholder":"Email Address", "style":" margin-bottom: 10px;"})
            # 'user_name':TextInput(attrs={"type":"text" , "name" :"log_username" , "class":"required form-control"  , "placeholder":"Email Address" , "style":" margin-bottom: 10px;"})
        }
    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
