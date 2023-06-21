from django import forms

from core.models import Students


class StudentRegForm(forms.ModelForm):
    verify_image = forms.BooleanField(required=False)
    tt_number = forms.CharField(max_length=50, required=False, disabled=True)

    class Meta:
        model = Students
        fields = ['tt_number']
