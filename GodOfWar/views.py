from django.shortcuts import render
from django.http import HttpResponseRedirect
from GodOfWar import forms
from GodOfWar.forms import RegistrationForm

def RegiFormView(request):
    form = forms.RegistrationForm()
    if request.method == 'POST':
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            print("Your Data is :")
            print(form.cleaned_data['Username'])
            #print(form.cleaned_data['Password'])
            print(form.cleaned_data['Email'])
            print(form.cleaned_data['Address'])
            print(form.cleaned_data['City'])
            print(form.cleaned_data['State'])
            print(form.cleaned_data['PinCode'])
            print(form.cleaned_data['DateOfBirth'])
            return HttpResponseRedirect('/ThankYou')
    else:
        form = RegistrationForm()
    return render(request,'MyApp/home.html',{'form':form})

def ThanksView(request):
    return render(request,'MyApp/thanks.html')