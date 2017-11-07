from django import forms


class CoverForm(forms.Form):
    title = forms.CharField()
    top_text = forms.CharField()
    author = forms.CharField()

