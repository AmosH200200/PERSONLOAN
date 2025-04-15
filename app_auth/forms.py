from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label = "Nom d'utilisateur",widget = forms.TextInput(attrs={'class':'form-control'}))
    pwd = forms.CharField(label = "Mot de passe",widget = forms.PasswordInput (attrs={'class':'form-control'}))

class RegisterForm(forms.Form):
    username = forms.CharField(label = "Nom d'utilisateur",widget = forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(label = "E-mail",widget = forms.EmailInput(attrs={'class':'form-control'}))
    pwd = forms.CharField(label = "Mot de passe",widget = forms.PasswordInput (attrs={'class':'form-control'}))    
    pwd_confirm = forms.CharField(label = "Confirmer mot de passe",widget = forms.PasswordInput (attrs={'class':'form-control'}))    
    