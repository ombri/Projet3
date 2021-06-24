from django import forms


class SignForm(forms.Form):
    F_username = forms.CharField(label='F_username', max_length=50)
    F_Fname = forms.CharField(label='F_Fname', max_length=50)
    F_Lname = forms.CharField(label='F_Lname', max_length=50)
    F_email = forms.CharField(label='F_email', max_length=50)
    F_password = forms.CharField(label='F_password', max_length=50)

    conf_password = forms.CharField(label='conf_password', max_length=50)


class LogForm(forms.Form):
    check_username = forms.CharField(label='check_username', max_length=50)
    check_password = forms.CharField(label='check_password', max_length=50)