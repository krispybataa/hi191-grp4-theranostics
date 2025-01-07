from django import forms
from .models import *
from django.core.exceptions import ValidationError

# ADDING DATA
def validate_positive(value, field_name):
    if value and value <= 0:
        raise ValidationError(f'{field_name} must be a positive value')
    return value

class AddTherapy(forms.ModelForm):
    class Meta:
        model = Therapy
        fields = ['date_of_psma','premedications','medications','furosemide','systolic', 'diastolic', 'hr', 'rr', 'saturation', 'date_therapy', 'radiopharm', 'side_effects']
        widgets = {
            'date_of_psma': forms.DateInput(attrs={'type': 'date'}),
            'date_therapy': forms.DateInput(attrs={'type': 'date'}),
            'systolic': forms.NumberInput(attrs={'min': '1'}),
            'diastolic': forms.NumberInput(attrs={'min': '1'}),
            'hr': forms.NumberInput(attrs={'min': '1'}),
            'rr': forms.NumberInput(attrs={'min': '1'}),
            'saturation': forms.NumberInput(attrs={'min': '1', 'max': '100'})
        }
        labels = {
            'date_of_psma' : 'Date of PSMA',
            'systolic' : 'Systolic BP(mmHg)',
            'diastolic' : 'Diastolic BP(mmHg)',
            'hr' : 'Heart Rate(bpm)',
            'rr' : 'Respiratory Rate(bpm)',
            'saturation' : 'Oxygen Saturation(%)'
        }

    def clean_systolic(self):
        return validate_positive(self.cleaned_data['systolic'], 'Systolic BP')

    def clean_diastolic(self):
        return validate_positive(self.cleaned_data['diastolic'], 'Diastolic BP')

    def clean_hr(self):
        return validate_positive(self.cleaned_data['hr'], 'Heart Rate')

    def clean_rr(self):
        return validate_positive(self.cleaned_data['rr'], 'Respiratory Rate')

    def clean_saturation(self):
        saturation = self.cleaned_data['saturation']
        if saturation and (saturation <= 0 or saturation > 100):
            raise ValidationError('Oxygen Saturation must be between 1 and 100')
        return saturation

class EditTherapy(forms.ModelForm):
    class Meta:
        model = Therapy
        fields = ['date_of_psma','premedications','medications','furosemide','systolic', 'diastolic', 'hr', 'rr', 'saturation', 'date_therapy', 'radiopharm', 'side_effects']
        widgets = {
            'date_of_psma': forms.DateInput(attrs={'type': 'date'}),
            'date_therapy': forms.DateInput(attrs={'type': 'date'}),
            'systolic': forms.NumberInput(attrs={'min': '1'}),
            'diastolic': forms.NumberInput(attrs={'min': '1'}),
            'hr': forms.NumberInput(attrs={'min': '1'}),
            'rr': forms.NumberInput(attrs={'min': '1'}),
            'saturation': forms.NumberInput(attrs={'min': '1', 'max': '100'})
        }
        labels = {
            'date_of_psma' : 'Date of PSMA',
            'systolic' : 'Systolic BP(mmHg)',
            'diastolic' : 'Diastolic BP(mmHg)',
            'hr' : 'Heart Rate(bpm)',
            'rr' : 'Respiratory Rate(bpm)',
            'saturation' : 'Oxygen Saturation(%)'
        }

    def clean_systolic(self):
        return validate_positive(self.cleaned_data['systolic'], 'Systolic BP')

    def clean_diastolic(self):
        return validate_positive(self.cleaned_data['diastolic'], 'Diastolic BP')

    def clean_hr(self):
        return validate_positive(self.cleaned_data['hr'], 'Heart Rate')

    def clean_rr(self):
        return validate_positive(self.cleaned_data['rr'], 'Respiratory Rate')

    def clean_saturation(self):
        saturation = self.cleaned_data['saturation']
        if saturation and (saturation <= 0 or saturation > 100):
            raise ValidationError('Oxygen Saturation must be between 1 and 100')
        return saturation
