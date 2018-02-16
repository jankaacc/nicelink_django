from django import forms


class LinkForm(forms.Form):
    oryginal_link = forms.URLField(label='Your link', max_length=200)
    nice_link = ''

