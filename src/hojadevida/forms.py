from django import forms
from src.hojadevida.models import Curriculum

class CurriculumForms(forms.ModelForm):
    class Meta:
        model = Curriculum
        fields = ['content']