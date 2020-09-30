from django import forms

STATES = ((1, 'India'),(2, 'New Zealand'),(3, 'Australia'),(4, 'SriLanka'),(5, 'England'),(6, 'South Africa'),(7, 'America'),(8, 'Other'),)


class RegistrationForm(forms.Form):
    Username = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder':'Enter Your Name'}))
    Password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter Your Password'}))
    Email = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Your Email'}))
    Address = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Ameerpet Hyderabad,Sri Chandra Boys Hostel,412'}))
    City = forms.CharField()
    State = forms.ChoiceField(choices=STATES,required=False)
    PinCode = forms.CharField()
    DateOfBirth = forms.DateField()
    date = forms.DateTimeInput()
    CheckMeOut = forms.BooleanField(required=False)
