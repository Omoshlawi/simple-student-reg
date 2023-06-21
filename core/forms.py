from django import forms

from core.models import Students


class StudentRegForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['tt_number']