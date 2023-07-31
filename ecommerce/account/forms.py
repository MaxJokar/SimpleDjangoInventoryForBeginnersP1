from django import forms
from .models import CustomUser
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError


#4. These codes are special for  customizing the Admin Panel :
class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        #  the name of model for which the form is made
        model = CustomUser
        fields = ('email', 'name', 'family','mobile_number','gender')


#5. To validate password 2:Responsible to check passwords(this function will be used for the validation)
    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2



#Saving with commit=False gets you a model object, then you can add your extra data and save it.
#6.  to change previous password(commit = True ,To permanent save)
    def save(self, commit=True):

        # Temporarily make an object to be add some
        # logic into the data if there is such a need
        # before writing to the database
        # return an object that hasn't yet been saved to the database.
        user = super().save(commit=False)
        #cleaned_data :automatically converts data to the appropriate type
        user.set_password(self.cleaned_data["password1"])
        if commit: #If it's True
            # Finally write the changes into database
            user.save()
        return user



#7.To set or change the fields(USER , Staff ) in Admin Panel :
class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """
    password = ReadOnlyPasswordHashField(help_text="To change Password , <a href ='../password'>Click Here </a> ")

    class Meta:
        model = CustomUser
        fields = ('email', 'name', 'family','mobile_number','gender', 'is_active', 'is_admin')

#=============================================================Admin Panel is over =================================================================================================
Choice_Gender=(("True","man"),("False","woman"))
# OUR WEBSITE FORM:
#1.  Common User(neither staff nor Admin ) Be able to register , log on with restriction
class RegisterUserForm(forms.Form):
    email = forms.EmailField(label = "",
                             error_messages={'required':'This field is NECESSARY',
                             'invalid':'This email is ivalid'},
                            widget=forms.TextInput(attrs={'class':'form_control', 'placeholder':'Email'}))
    name = forms.CharField(label=""
                           , widget=forms.TextInput(attrs={'class':'form_control', 'placeholder':'Name'}))
    family =forms.CharField(label="",
                            error_messages={'required ':'This field is necessary'}
                            , widget=forms.TextInput(attrs={'class':'form_control', 'placeholder':'Family'}))
    mobile_number = forms.CharField(label="",
                                    error_messages={'required':'This field is necessary'}
                                    , widget=forms.TextInput(attrs={'class':'form_control', 'placeholder':'Mobile Number'}))
    gender = forms.ChoiceField(label="", choices=Choice_Gender,
                               )
    password = forms.CharField(label="",
                               error_messages={'required':'This field is necessary'}
                               ,widget=forms.TextInput(attrs={'class':'form_control', 'placeholder':'password'}))


    confirm_password = forms.CharField(label="",
                               error_messages={'required':'This field is necessary'}
                               ,widget=forms.TextInput(attrs={'class':'form_control', 'placeholder':'confirm password'}))


#==== this function will be used for the validation=====check for validation =======================================================
#2.  for the validation
# If Perviously a USER had registered witha the SAME EMAIL ,this function does not let  to register with the same EMAIL
    # We Only want to inquire the specific field
    def clean_email(self):  # sourcery skip: use-named-expression
        email=self.cleaned_data['email']# or get('email') :impossible to login with a repetitive email
        flag = CustomUser.objects.filter(email=email).exists() # search in db exists or not: True or False
        if flag : #if it True:
            raise ValidationError('This email was registered BEFORE')
        return email

    #2.1 The same for Mobile_number:validation
    # We Only want to inquire the specific field :clean_name of that field
    def clean_mobile_number(self):  # sourcery skip: use-named-expression
        mobile_number = self.cleaned_data['mobile_number'] # returns a dictionary of validated form input fields and their values
        flag2 = CustomUser.objects.filter(mobile_number=mobile_number).exists()
        if flag2 :
            raise ValidationError('This email was registered BEFORE')
        return mobile_number

#2.2 this function will be used for the validation
# clean means we want to inquire all
    def clean(self):  # sourcery skip: use-named-expression
        password =self.cleaned_data.get('password')
        confirm_password=self.cleaned_data.get('confirm_password')
        if password and confirm_password and password!=confirm_password :
            raise ValidationError('password & confirm are not THE SAME')
        # ?????? need return??????????????????????????????????



#==============================================================================================================================

# We have already declared model , So defining Model is not necessary again , only a form enough:
class LoginUserForm(forms.Form):
    email = forms.EmailField(label = "",
                             error_messages={'required':'This field is Necessary !'}
                            ,widget=forms.TextInput(attrs={'class':'form_control', 'placeholder':'email@gmail.com'}))
    password = forms.CharField(label="",
                               error_messages={'required':'Password is Necessary!'}
                               ,widget=forms.TextInput(attrs={'class':'form_control', 'placeholder':'password'}))
