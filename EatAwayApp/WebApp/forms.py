from .models import ConsumptionItem
from django import forms


class WorkerForm(forms.ModelForm):
    birthdate = forms.DateField(input_formats=['%d/%m/%Y'])
    class Meta:
        model = ConsumptionItem
        fields = ('__all__')