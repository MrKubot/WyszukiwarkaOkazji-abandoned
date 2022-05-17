from django import forms


class DaneProduktu(forms.Form):
    nazwa = forms.CharField(max_length=150, required=True)
    URL_OLX = forms.URLField(required=True)
    URL_CENEO = forms.URLField(required=True)
    URL_VINTED = forms.URLField(required=True)
    SCD = forms.IntegerField(required=False)
