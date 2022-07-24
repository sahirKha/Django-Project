from django import forms



class contactform(forms.Form):
    subject=forms.CharField()
    from_email=forms.EmailField(required=True)
    message=forms.CharField(widget=forms.Textarea, required=True)