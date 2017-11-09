from urllib.parse import urlencode
from django import forms


class CoverForm(forms.Form):
    title = forms.CharField()
    top_text = forms.CharField()
    author = forms.CharField()
    animal_code = forms.ChoiceField(choices=[(i, i) for i in range(1, 41)])
    color_code = forms.ChoiceField(choices=[(i, i) for i in range(0, 17)])
    guide_text = forms.CharField()
    guide_text_placement = forms.ChoiceField(
        choices=[
            ('bottom_right', 'bottom_right'),
            ('bottom_left', 'bottom_left'),
            ('top_right', 'top_right'),
            ('top_left', 'top_left'),
        ])

    @property
    def get_params(self):
        if hasattr(self, 'cleaned_data'):
            return urlencode(self.cleaned_data)
        return None

