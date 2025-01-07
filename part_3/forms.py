from .models import *
from django import forms
from django.forms import ModelChoiceField, ModelForm

# ADDING DATA
class AddPostTherapy(ModelForm):
    class Meta:
        model = PostTherapy
        fields = ['date_of_post_therapy','post_therapy_scan_hours','with_spect_ct','lesions','bone_lesion_details', 'lesion_image', 'salivary_gland', 'kidney_left', 'kidney_right', 'dosimetry_image']
        widgets = {
            'date_of_post_therapy': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'with_spect_ct': 'With SPECT/CT',
            'post_therapy_scan_hours': 'Therapy Scan Duration (in Hours)'
        }

class EditPostTherapy(ModelForm):
    class Meta:
        model = PostTherapy
        fields = ['date_of_post_therapy','post_therapy_scan_hours','with_spect_ct','lesions','bone_lesion_details', 'lesion_image', 'salivary_gland', 'kidney_left', 'kidney_right', 'dosimetry_image']
        widgets = {
            'date_of_post_therapy': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'with_spect_ct': 'With SPECT/CT',
            'post_therapy_scan_hours': 'Therapy Scan Duration (in Hours)'
        }
        def clean_salivary_gland(self):
            salivary_gland = self.cleaned_data['salivary_gland']
            if salivary_gland < 0:
                raise forms.ValidationError("Salivary gland must be a positive value")
            return salivary_gland
        def clean_kidney_left(self):
            kidney_left = self.cleaned_data['kidney_left']
            if kidney_left < 0:
                raise forms.ValidationError("Left kidney must be a positive value")
            return kidney_left
        def clean_kidney_right(self):
            kidney_right = self.cleaned_data['kidney_right']
            if kidney_right < 0:
                raise forms.ValidationError("Right kidney must be a positive value")
            return kidney_right
