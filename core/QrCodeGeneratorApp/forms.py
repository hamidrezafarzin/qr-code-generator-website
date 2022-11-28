from django import forms

class GeneratorForm(forms.Form):
    text = forms.CharField()