from django import forms
from .models import Student

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150 , required=True , widget=forms.TextInput(attrs={'placeholder' : 'Enter Username'}))
    password = forms.CharField(max_length=200 , required=True , widget=forms.PasswordInput(attrs={'placeholder' : 'Enter Paswword'}))

class RegisterForm(forms.Form):
    name = forms.CharField(max_length=100 , required=True , widget=forms.TextInput(attrs={'palaceholder': 'Enter Your Name'}))
    username = forms.CharField(max_length=150 , required=True , widget=forms.TextInput(attrs={'placeholder' : 'Enter Username'}))
    password = forms.CharField(max_length=200 , required=True , widget=forms.PasswordInput(attrs={'placeholder' : 'Enter Paswword'}))

    

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name' , 'subject' , 'marks']
        widgets = {
            'name' : forms.TextInput(attrs={'placeholder' : 'Student Name'}),
            'subject' : forms.TextInput(attrs={'placeholder' : 'Student Subject'}),
            'marks' : forms.TextInput(attrs={'placeholder' : 'Student Marks Between(0 - 100)'}),
        }


    def clean_marks(self):
        marks = self.cleaned_data.get("marks")
        if not (0 < marks < 100 ):
            raise forms.ValidationError("Marks must be between 0 and 100")
        
        return marks
    


        

