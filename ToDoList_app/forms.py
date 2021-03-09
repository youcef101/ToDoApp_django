from django.forms import ModelForm
from .models import *
class ActivityForm(ModelForm):
    class Meta:
        model=Activity
        fields='__all__'