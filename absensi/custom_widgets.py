# custom_widgets.py
from django import forms

class CheckboxSelectMultiple(forms.CheckboxSelectMultiple):
    def render(self, name, value, attrs=None, renderer=None):
        if value is None:
            value = []
        return super().render(name, value, attrs, renderer)
