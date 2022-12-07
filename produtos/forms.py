from django import forms
from produtos.models import Usuario

class DatePickerInput(forms.DateInput):
        input_type = 'date'

class TimePickerInput(forms.TimeInput):
        input_type = 'time'

class UsuarioForm(forms.ModelForm):

    class Meta:
        model= Usuario
        fields= '_all_'
    
        widgets = {
            'minicursos': forms.CheckboxSelectMultiple(),
            'sexo': forms.RadioSelect(),
            'nascimento': forms.TimeInput(attrs={'type': 'date'}),
        }