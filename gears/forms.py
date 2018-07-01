from django import forms
from gears.models import Gear

class add_gearForm(forms.ModelForm):
    class Meta:
        model =Gear
        fields = ['gear_type','gear_producer','gear_name','gear_model','gear_quality','gear_availablity','gear_price']

