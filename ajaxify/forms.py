from django.forms import ModelForm
from .models import contect

class Newform(ModelForm):
    class Meta:
        model =contect
        fields ='__all__'
