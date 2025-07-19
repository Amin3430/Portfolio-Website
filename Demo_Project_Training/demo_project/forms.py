from django import forms

class UserForm(forms.Form):
    candidate_name = forms.CharField(max_length=100)
    contact = forms.CharField(label= "Contact")
    email = forms.EmailField(label= "Email")
    expected_ctc = forms.CharField(label= "Expected CTC")
