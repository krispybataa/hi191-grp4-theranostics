from .models import *
from django import forms
from django.forms import ModelChoiceField, ModelForm

# ADDING DATA
class AddPatient(ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'age', 'address', 'diagnosis_date', 'surgery_date', 'histopath_result', 'histopath_details', 'gleason_score', 'date_of_treatment', 'type_of_treatment']
        widgets = {
            'diagnosis_date': forms.DateInput(attrs={'type': 'date'}),
            'surgery_date': forms.DateInput(attrs={'type': 'date'}),
            'date_of_treatment': forms.DateInput(attrs={'type': 'date'}),
        }
        

class EditPatient(ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'age', 'address', 'diagnosis_date', 'surgery_date', 'histopath_result', 'histopath_details', 'gleason_score', 'date_of_treatment', 'type_of_treatment']
        widgets = {
            'diagnosis_date': forms.DateInput(attrs={'type': 'date'}),
            'surgery_date': forms.DateInput(attrs={'type': 'date'}),
            'date_of_treatment': forms.DateInput(attrs={'type': 'date'}),
        }

class EditPhysicalExam(ModelForm):
    class Meta:
        model = PhysicalExam
        fields = ['ecog_score', 'height', 'weight', 'bmi', 'bp', 'hr', 'pain_score', 'local_symptoms', 'systemic_symptoms']
        labels = {
            'height': 'Height(cm)',
            'weight': 'Weight(kg)',
            'bmi': 'BMI',
            'bp' : 'Blood Pressure(mmHg)',
            'hr' : 'Heart Rate(bpm)'
        }
        widgets = {
            'bmi': forms.NumberInput(attrs={'readonly': 'readonly'})
        }

    def clean(self):
        cleaned_data = super().clean()
        height = cleaned_data.get('height')
        weight = cleaned_data.get('weight')
        
        if height and weight:
            # Convert height from cm to meters
            height_in_meters = height / 100
            # Calculate BMI and round to nearest integer
            bmi = round(weight / (height_in_meters * height_in_meters))
            cleaned_data['bmi'] = bmi
            
        return cleaned_data

class AddPhysicalExam(ModelForm):
    class Meta:
        model = PhysicalExam
        fields = ['ecog_score', 'height', 'weight', 'bmi', 'bp', 'hr', 'pain_score', 'local_symptoms', 'systemic_symptoms']
        labels = {
            'height': 'Height(cm)',
            'weight': 'Weight(kg)',
            'bmi': 'BMI',
            'bp' : 'Blood Pressure(mmHg)',
            'hr' : 'Heart Rate(bpm)'
        }
        widgets = {
            'bmi': forms.NumberInput(attrs={'readonly': 'readonly'})
        }
        
    def clean(self):
        cleaned_data = super().clean()
        height = cleaned_data.get('height')
        weight = cleaned_data.get('weight')
        
        if height and weight:
            # Convert height from cm to meters
            height_in_meters = height / 100
            # Calculate BMI and round to nearest integer
            bmi = round(weight / (height_in_meters * height_in_meters))
            cleaned_data['bmi'] = bmi
            
        return cleaned_data

class AddScreening(ModelForm):
    class Meta:
        model = Screening
        fields = ['psa', 'creatinine', 'wbc', 'rbc', 'hemoglobin', 'hematocrit', 'platelet', 'lactate_hydrogenase', 'alkaline_phosphatase', 'sgpt', 'sgot', 'bilirubins', 
        'salivary_gland_status', 'salivary_gland_image', 'bone_metastasis_status', 'bone_scan_image', 'renal_scintigraphy', 'gapsma_choices', 'gapsma_img', 
        'gapsma_prostate_lesion_status', 'gapsma_prostate_location', 'gapsma_prostate_suv', 'gapsma_prostate_size',
        'gapsma_lymph_node_lesion_status', 'gapsma_lymph_node_location', 'gapsma_lymph_node_suv', 'gapsma_lymph_node_size',
        'gapsma_bone_lesion_status', 'gapsma_bone_location', 'gapsma_bone_suv', 'gapsma_bone_size',
        'gapsma_brain_lesion_status', 'gapsma_brain_location', 'gapsma_brain_suv', 'gapsma_brain_size',
        'gapsma_lung_lesion_status', 'gapsma_lung_location', 'gapsma_lung_suv', 'gapsma_lung_size',
        'gapsma_liver_lesion_status', 'gapsma_liver_location', 'gapsma_liver_suv', 'gapsma_liver_size',
        'fdgpetct_img',
        'fdgpetct_prostate_lesion_status', 'fdgpetct_prostate_location', 'fdgpetct_prostate_suv', 'fdgpetct_prostate_size',
        'fdgpetct_lymph_node_lesion_status', 'fdgpetct_lymph_node_location', 'fdgpetct_lymph_node_suv', 'fdgpetct_lymph_node_size',
        'fdgpetct_bone_lesion_status', 'fdgpetct_bone_location', 'fdgpetct_bone_suv', 'fdgpetct_bone_size',
        'fdgpetct_brain_lesion_status', 'fdgpetct_brain_location', 'fdgpetct_brain_suv', 'fdgpetct_brain_size',
        'fdgpetct_lung_lesion_status', 'fdgpetct_lung_location', 'fdgpetct_lung_suv', 'fdgpetct_lung_size',
        'fdgpetct_liver_lesion_status', 'fdgpetct_liver_location', 'fdgpetct_liver_suv', 'fdgpetct_liver_size',
        'assessment', 'plan']
        labels = {
            'psa': 'PSA',
            'creatinine': 'Creatinine(mg/dL)',
            'wbc': 'WBC',
            'rbc' : 'RBC',
            'hemoglobin' : 'Hemogoblin(g/dL)',
            'hematocrit' : 'Hematocrit(%)',
            'platelet' : 'Platelet Count(mcL)',
            'lactate_hydrogenase' : 'Lactate Hydrogenase(units/L)',
            'alkaline_phosphatase' : 'Alkaline Phosphatase(units/L)', 
            'sgpt' : 'SGPT(units/L)', 
            'sgot' : 'SGOT(units/L)', 
            'bilirubins' : 'Bilirubins(mg/dL)',
            'salivary_gland_status': 'Salivary Gland Status',
            'salivary_gland_image': 'Salivary Gland Image',
            'bone_metastasis_status': 'Bone Metastasis Status',
            'bone_scan_image': 'Bone Scan Image',
            'renal_scintigraphy': 'Renal Scintigraphy',
            'gapsma_choices': 'GA PSMA Type',
            'gapsma_img': 'GA PSMA Image',
            'assessment': 'Assessment',
            'plan': 'Plan'
        }
        widgets = {
            'psa': forms.NumberInput(attrs={'step': 'any'}),
            'creatinine': forms.NumberInput(attrs={'step': 'any'}),
            'wbc': forms.NumberInput(attrs={'step': 'any'}),
            'rbc': forms.NumberInput(attrs={'step': 'any'}),
            'hemoglobin': forms.NumberInput(attrs={'step': 'any'}),
            'hematocrit': forms.NumberInput(attrs={'step': 'any'}),
            'platelet': forms.NumberInput(attrs={'step': 'any'}),
            'lactate_hydrogenase': forms.NumberInput(attrs={'step': 'any'}),
            'alkaline_phosphatase': forms.NumberInput(attrs={'step': 'any'}),
            'sgpt': forms.NumberInput(attrs={'step': 'any'}),
            'sgot': forms.NumberInput(attrs={'step': 'any'}),
            'bilirubins': forms.NumberInput(attrs={'step': 'any'}),
            'gapsma_prostate_suv': forms.NumberInput(attrs={'step': 'any'}),
            'gapsma_prostate_size': forms.NumberInput(attrs={'step': 'any'}),
            'gapsma_lymph_node_suv': forms.NumberInput(attrs={'step': 'any'}),
            'gapsma_lymph_node_size': forms.NumberInput(attrs={'step': 'any'}),
            'gapsma_bone_suv': forms.NumberInput(attrs={'step': 'any'}),
            'gapsma_bone_size': forms.NumberInput(attrs={'step': 'any'}),
            'gapsma_brain_suv': forms.NumberInput(attrs={'step': 'any'}),
            'gapsma_brain_size': forms.NumberInput(attrs={'step': 'any'}),
            'gapsma_lung_suv': forms.NumberInput(attrs={'step': 'any'}),
            'gapsma_lung_size': forms.NumberInput(attrs={'step': 'any'}),
            'gapsma_liver_suv': forms.NumberInput(attrs={'step': 'any'}),
            'gapsma_liver_size': forms.NumberInput(attrs={'step': 'any'}),
            'fdgpetct_prostate_suv': forms.NumberInput(attrs={'step': 'any'}),
            'fdgpetct_prostate_size': forms.NumberInput(attrs={'step': 'any'}),
            'fdgpetct_lymph_node_suv': forms.NumberInput(attrs={'step': 'any'}),
            'fdgpetct_lymph_node_size': forms.NumberInput(attrs={'step': 'any'}),
            'fdgpetct_bone_suv': forms.NumberInput(attrs={'step': 'any'}),
            'fdgpetct_bone_size': forms.NumberInput(attrs={'step': 'any'}),
            'fdgpetct_brain_suv': forms.NumberInput(attrs={'step': 'any'}),
            'fdgpetct_brain_size': forms.NumberInput(attrs={'step': 'any'}),
            'fdgpetct_lung_suv': forms.NumberInput(attrs={'step': 'any'}),
            'fdgpetct_lung_size': forms.NumberInput(attrs={'step': 'any'}),
            'fdgpetct_liver_suv': forms.NumberInput(attrs={'step': 'any'}),
            'fdgpetct_liver_size': forms.NumberInput(attrs={'step': 'any'}),
            'assessment': forms.Textarea(attrs={'required': True}),
            'plan': forms.Textarea(attrs={'required': True}),
        }

class EditScreening(ModelForm):
    class Meta:
        model = Screening
        fields = ['psa', 'creatinine', 'wbc', 'rbc', 'hemoglobin', 'hematocrit', 'platelet', 'lactate_hydrogenase', 'alkaline_phosphatase', 'sgpt', 'sgot', 'bilirubins', 
        'salivary_gland_status', 'salivary_gland_image', 'bone_metastasis_status', 'bone_scan_image', 'renal_scintigraphy', 'gapsma_choices', 'gapsma_img', 
        'gapsma_prostate_lesion_status', 'gapsma_prostate_location', 'gapsma_prostate_suv', 'gapsma_prostate_size',
        'gapsma_lymph_node_lesion_status', 'gapsma_lymph_node_location', 'gapsma_lymph_node_suv', 'gapsma_lymph_node_size',
        'gapsma_bone_lesion_status', 'gapsma_bone_location', 'gapsma_bone_suv', 'gapsma_bone_size',
        'gapsma_brain_lesion_status', 'gapsma_brain_location', 'gapsma_brain_suv', 'gapsma_brain_size',
        'gapsma_lung_lesion_status', 'gapsma_lung_location', 'gapsma_lung_suv', 'gapsma_lung_size',
        'gapsma_liver_lesion_status', 'gapsma_liver_location', 'gapsma_liver_suv', 'gapsma_liver_size',
        'fdgpetct_img',
        'fdgpetct_prostate_lesion_status', 'fdgpetct_prostate_location', 'fdgpetct_prostate_suv', 'fdgpetct_prostate_size',
        'fdgpetct_lymph_node_lesion_status', 'fdgpetct_lymph_node_location', 'fdgpetct_lymph_node_suv', 'fdgpetct_lymph_node_size',
        'fdgpetct_bone_lesion_status', 'fdgpetct_bone_location', 'fdgpetct_bone_suv', 'fdgpetct_bone_size',
        'fdgpetct_brain_lesion_status', 'fdgpetct_brain_location', 'fdgpetct_brain_suv', 'fdgpetct_brain_size',
        'fdgpetct_lung_lesion_status', 'fdgpetct_lung_location', 'fdgpetct_lung_suv', 'fdgpetct_lung_size',
        'fdgpetct_liver_lesion_status', 'fdgpetct_liver_location', 'fdgpetct_liver_suv', 'fdgpetct_liver_size',
        'assessment', 'plan']
        labels = {
            'psa': 'PSA',
            'creatinine': 'Creatinine(mg/dL)',
            'wbc': 'WBC',
            'rbc' : 'RBC',
            'hemoglobin' : 'Hemogoblin(g/dL)',
            'hematocrit' : 'Hematocrit(%)',
            'platelet' : 'Platelet Count(mcL)',
            'lactate_hydrogenase' : 'Lactate Hydrogenase(units/L)',
            'alkaline_phosphatase' : 'Alkaline Phosphatase(units/L)', 
            'sgpt' : 'SGPT(units/L)', 
            'sgot' : 'SGOT(units/L)', 
            'bilirubins' : 'Bilirubins(mg/dL)',
            'salivary_gland_status': 'Salivary Gland Status',
            'salivary_gland_image': 'Salivary Gland Image',
            'bone_metastasis_status': 'Bone Metastasis Status',
            'bone_scan_image': 'Bone Scan Image',
            'renal_scintigraphy': 'Renal Scintigraphy',
            'gapsma_choices': 'GA PSMA Type',
            'gapsma_img': 'GA PSMA Image',
            'assessment': 'Assessment',
            'plan': 'Plan'
        }
        widgets = {
            'psa': forms.NumberInput(attrs={'step': 'any'}),
            'creatinine': forms.NumberInput(attrs={'step': 'any'}),
            'wbc': forms.NumberInput(attrs={'step': 'any'}),
            'rbc': forms.NumberInput(attrs={'step': 'any'}),
            'hemoglobin': forms.NumberInput(attrs={'step': 'any'}),
            'hematocrit': forms.NumberInput(attrs={'step': 'any'}),
            'platelet': forms.NumberInput(attrs={'step': 'any'}),
            'lactate_hydrogenase': forms.NumberInput(attrs={'step': 'any'}),
            'alkaline_phosphatase': forms.NumberInput(attrs={'step': 'any'}),
            'sgpt': forms.NumberInput(attrs={'step': 'any'}),
            'sgot': forms.NumberInput(attrs={'step': 'any'}),
            'bilirubins': forms.NumberInput(attrs={'step': 'any'}),
            'gapsma_prostate_suv': forms.NumberInput(attrs={'step': 'any'}),
            'gapsma_prostate_size': forms.NumberInput(attrs={'step': 'any'}),
            'gapsma_lymph_node_suv': forms.NumberInput(attrs={'step': 'any'}),
            'gapsma_lymph_node_size': forms.NumberInput(attrs={'step': 'any'}),
            'gapsma_bone_suv': forms.NumberInput(attrs={'step': 'any'}),
            'gapsma_bone_size': forms.NumberInput(attrs={'step': 'any'}),
            'gapsma_brain_suv': forms.NumberInput(attrs={'step': 'any'}),
            'gapsma_brain_size': forms.NumberInput(attrs={'step': 'any'}),
            'gapsma_lung_suv': forms.NumberInput(attrs={'step': 'any'}),
            'gapsma_lung_size': forms.NumberInput(attrs={'step': 'any'}),
            'gapsma_liver_suv': forms.NumberInput(attrs={'step': 'any'}),
            'gapsma_liver_size': forms.NumberInput(attrs={'step': 'any'}),
            'fdgpetct_prostate_suv': forms.NumberInput(attrs={'step': 'any'}),
            'fdgpetct_prostate_size': forms.NumberInput(attrs={'step': 'any'}),
            'fdgpetct_lymph_node_suv': forms.NumberInput(attrs={'step': 'any'}),
            'fdgpetct_lymph_node_size': forms.NumberInput(attrs={'step': 'any'}),
            'fdgpetct_bone_suv': forms.NumberInput(attrs={'step': 'any'}),
            'fdgpetct_bone_size': forms.NumberInput(attrs={'step': 'any'}),
            'fdgpetct_brain_suv': forms.NumberInput(attrs={'step': 'any'}),
            'fdgpetct_brain_size': forms.NumberInput(attrs={'step': 'any'}),
            'fdgpetct_lung_suv': forms.NumberInput(attrs={'step': 'any'}),
            'fdgpetct_lung_size': forms.NumberInput(attrs={'step': 'any'}),
            'fdgpetct_liver_suv': forms.NumberInput(attrs={'step': 'any'}),
            'fdgpetct_liver_size': forms.NumberInput(attrs={'step': 'any'}),
            'assessment': forms.Textarea(attrs={'required': True}),
            'plan': forms.Textarea(attrs={'required': True}),
        }