from django import forms
from .models import *
from django.core.exceptions import ValidationError

# ADDING DATA
class AddPatient(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'age', 'address', 'diagnosis_date', 'surgery_date', 'histopath_result', 'histopath_details', 'gleason_score', 'date_of_treatment', 'type_of_treatment']
        widgets = {
            'diagnosis_date': forms.DateInput(attrs={'type': 'date'}),
            'surgery_date': forms.DateInput(attrs={'type': 'date'}),
            'date_of_treatment': forms.DateInput(attrs={'type': 'date'}),
            'age': forms.NumberInput(attrs={'min': '0', 'type': 'number'}),
            'gleason_score': forms.NumberInput(attrs={'min': '0', 'type': 'number'}),
        }
        
    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age is None:
            raise ValidationError('Age is required')
        if age < 0:
            raise ValidationError('Age must be a positive number')
        return age

    def clean_gleason_score(self):
        score = self.cleaned_data.get('gleason_score')
        if score is None:
            raise ValidationError('Gleason score is required')
        if score < 0:
            raise ValidationError('Gleason score must be a positive number')
        return score

class EditPatient(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'age', 'address', 'diagnosis_date', 'surgery_date', 'histopath_result', 'histopath_details', 'gleason_score', 'date_of_treatment', 'type_of_treatment']
        widgets = {
            'diagnosis_date': forms.DateInput(attrs={'type': 'date'}),
            'surgery_date': forms.DateInput(attrs={'type': 'date'}),
            'date_of_treatment': forms.DateInput(attrs={'type': 'date'}),
            'age': forms.NumberInput(attrs={'min': '0', 'type': 'number'}),
            'gleason_score': forms.NumberInput(attrs={'min': '0', 'type': 'number'}),
        }

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age is None:
            raise ValidationError('Age is required')
        if age < 0:
            raise ValidationError('Age must be a positive number')
        return age

    def clean_gleason_score(self):
        score = self.cleaned_data.get('gleason_score')
        if score is None:
            raise ValidationError('Gleason score is required')
        if score < 0:
            raise ValidationError('Gleason score must be a positive number')
        return score

class AddPhysicalExam(forms.ModelForm):
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
            'ecog_score': forms.NumberInput(attrs={'min': '1'}),
            'height': forms.NumberInput(attrs={'min': '1'}),
            'weight': forms.NumberInput(attrs={'min': '1'}),
            'bmi': forms.NumberInput(attrs={'readonly': 'readonly', 'step': '0.0001', 'min': '0.1'}),
            'hr': forms.NumberInput(attrs={'min': '1'}),
            'pain_score': forms.NumberInput(attrs={'min': '1'})
        }

    def clean(self):
        cleaned_data = super().clean()
        height = cleaned_data.get('height')
        weight = cleaned_data.get('weight')

        if height and weight:
            bmi = round((weight / ((height/100) ** 2)), 4)
            cleaned_data['bmi'] = bmi

        return cleaned_data

    def clean_ecog_score(self):
        ecog_score = self.cleaned_data['ecog_score']
        if ecog_score < 0:
            raise ValidationError('ECOG Score must be a positive value')
        return ecog_score

    def clean_height(self):
        height = self.cleaned_data['height']
        if height < 0:
            raise ValidationError('Height must be a positive value')
        return height

    def clean_weight(self):
        weight = self.cleaned_data['weight']
        if weight < 0:
            raise ValidationError('Weight must be a positive value')
        return weight

    def clean_hr(self):
        hr = self.cleaned_data['hr']
        if hr < 0:
            raise ValidationError('Heart Rate must be a positive value')
        return hr

    def clean_pain_score(self):
        pain_score = self.cleaned_data['pain_score']
        if pain_score < 0:
            raise ValidationError('Pain Score must be a positive value')
        return pain_score

class EditPhysicalExam(forms.ModelForm):
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
            'ecog_score': forms.NumberInput(attrs={'min': '1'}),
            'height': forms.NumberInput(attrs={'min': '1'}),
            'weight': forms.NumberInput(attrs={'min': '1'}),
            'bmi': forms.NumberInput(attrs={'readonly': 'readonly', 'step': '0.0001', 'min': '0.1'}),
            'hr': forms.NumberInput(attrs={'min': '1'}),
            'pain_score': forms.NumberInput(attrs={'min': '1'})
        }

    def clean_ecog_score(self):
        ecog_score = self.cleaned_data['ecog_score']
        if ecog_score < 0:
            raise ValidationError('ECOG Score must be a positive value')
        return ecog_score

    def clean_height(self):
        height = self.cleaned_data['height']
        if height < 0:
            raise ValidationError('Height must be a positive value')
        return height

    def clean_weight(self):
        weight = self.cleaned_data['weight']
        if weight < 0:
            raise ValidationError('Weight must be a positive value')
        return weight

    def clean_hr(self):
        hr = self.cleaned_data['hr']
        if hr < 0:
            raise ValidationError('Heart Rate must be a positive value')
        return hr

    def clean_pain_score(self):
        pain_score = self.cleaned_data['pain_score']
        if pain_score < 0:
            raise ValidationError('Pain Score must be a positive value')
        return pain_score

class AddScreening(forms.ModelForm):
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
            'psa': forms.NumberInput(attrs={'step': 'any', 'min': '0'}),
            'creatinine': forms.NumberInput(attrs={'step': 'any', 'min': '0'}),
            'wbc': forms.NumberInput(attrs={'step': 'any', 'min': '0'}),
            'rbc': forms.NumberInput(attrs={'step': 'any', 'min': '0'}),
            'hemoglobin': forms.NumberInput(attrs={'step': 'any', 'min': '0'}),
            'hematocrit': forms.NumberInput(attrs={'step': 'any', 'min': '0'}),
            'platelet': forms.NumberInput(attrs={'step': 'any', 'min': '0'}),
            'lactate_hydrogenase': forms.NumberInput(attrs={'step': 'any', 'min': '0'}),
            'alkaline_phosphatase': forms.NumberInput(attrs={'step': 'any', 'min': '0'}),
            'sgpt': forms.NumberInput(attrs={'step': 'any', 'min': '0'}),
            'sgot': forms.NumberInput(attrs={'step': 'any', 'min': '0'}),
            'bilirubins': forms.NumberInput(attrs={'step': 'any', 'min': '0'}),
            'gapsma_prostate_suv': forms.NumberInput(attrs={'step': 'any', 'min': '0'}),
            'gapsma_prostate_size': forms.NumberInput(attrs={'step': 'any', 'min': '0'}),
            'gapsma_lymph_node_suv': forms.NumberInput(attrs={'step': 'any', 'min': '0'}),
            'gapsma_lymph_node_size': forms.NumberInput(attrs={'step': 'any', 'min': '0'}),
            'gapsma_bone_suv': forms.NumberInput(attrs={'step': 'any', 'min': '0'}),
            'gapsma_bone_size': forms.NumberInput(attrs={'step': 'any', 'min': '0'}),
            'gapsma_brain_suv': forms.NumberInput(attrs={'step': 'any', 'min': '0'}),
            'gapsma_brain_size': forms.NumberInput(attrs={'step': 'any', 'min': '0'}),
            'gapsma_lung_suv': forms.NumberInput(attrs={'step': 'any', 'min': '0'}),
            'gapsma_lung_size': forms.NumberInput(attrs={'step': 'any', 'min': '0'}),
            'gapsma_liver_suv': forms.NumberInput(attrs={'step': 'any', 'min': '0'}),
            'gapsma_liver_size': forms.NumberInput(attrs={'step': 'any', 'min': '0'}),
            'fdgpetct_prostate_suv': forms.NumberInput(attrs={'step': 'any', 'min': '0'}),
            'fdgpetct_prostate_size': forms.NumberInput(attrs={'step': 'any', 'min': '0'}),
            'fdgpetct_lymph_node_suv': forms.NumberInput(attrs={'step': 'any', 'min': '0'}),
            'fdgpetct_lymph_node_size': forms.NumberInput(attrs={'step': 'any', 'min': '0'}),
            'fdgpetct_bone_suv': forms.NumberInput(attrs={'step': 'any', 'min': '0'}),
            'fdgpetct_bone_size': forms.NumberInput(attrs={'step': 'any', 'min': '0'}),
            'fdgpetct_brain_suv': forms.NumberInput(attrs={'step': 'any', 'min': '0'}),
            'fdgpetct_brain_size': forms.NumberInput(attrs={'step': 'any', 'min': '0'}),
            'fdgpetct_lung_suv': forms.NumberInput(attrs={'step': 'any', 'min': '0'}),
            'fdgpetct_lung_size': forms.NumberInput(attrs={'step': 'any', 'min': '0'}),
            'fdgpetct_liver_suv': forms.NumberInput(attrs={'step': 'any', 'min': '0'}),
            'fdgpetct_liver_size': forms.NumberInput(attrs={'step': 'any', 'min': '0'}),
            'assessment': forms.Select(choices=Screening.ASSESSMENT, attrs={'required': True}),
            'plan': forms.Textarea(attrs={'required': True}),
        }

    def clean_psa(self):
        psa = self.cleaned_data['psa']
        if psa < 0:
            raise ValidationError('PSA must be a positive value')
        return psa

    def clean_creatinine(self):
        creatinine = self.cleaned_data['creatinine']
        if creatinine < 0:
            raise ValidationError('Creatinine must be a positive value')
        return creatinine

    def clean_wbc(self):
        wbc = self.cleaned_data['wbc']
        if wbc < 0:
            raise ValidationError('WBC must be a positive value')
        return wbc

    def clean_rbc(self):
        rbc = self.cleaned_data['rbc']
        if rbc < 0:
            raise ValidationError('RBC must be a positive value')
        return rbc

    def clean_hemoglobin(self):
        hemoglobin = self.cleaned_data['hemoglobin']
        if hemoglobin < 0:
            raise ValidationError('Hemoglobin must be a positive value')
        return hemoglobin

    def clean_hematocrit(self):
        hematocrit = self.cleaned_data['hematocrit']
        if hematocrit < 0:
            raise ValidationError('Hematocrit must be a positive value')
        return hematocrit

    def clean_platelet(self):
        platelet = self.cleaned_data['platelet']
        if platelet < 0:
            raise ValidationError('Platelet must be a positive value')
        return platelet

    def clean_lactate_hydrogenase(self):
        lactate_hydrogenase = self.cleaned_data['lactate_hydrogenase']
        if lactate_hydrogenase < 0:
            raise ValidationError('Lactate Hydrogenase must be a positive value')
        return lactate_hydrogenase

    def clean_alkaline_phosphatase(self):
        alkaline_phosphatase = self.cleaned_data['alkaline_phosphatase']
        if alkaline_phosphatase < 0:
            raise ValidationError('Alkaline Phosphatase must be a positive value')
        return alkaline_phosphatase

    def clean_sgpt(self):
        sgpt = self.cleaned_data['sgpt']
        if sgpt < 0:
            raise ValidationError('SGPT must be a positive value')
        return sgpt

    def clean_sgot(self):
        sgot = self.cleaned_data['sgot']
        if sgot < 0:
            raise ValidationError('SGOT must be a positive value')
        return sgot

    def clean_bilirubins(self):
        bilirubins = self.cleaned_data['bilirubins']
        if bilirubins < 0:
            raise ValidationError('Bilirubins must be a positive value')
        return bilirubins

    def clean_gapsma_prostate_suv(self):
        gapsma_prostate_suv = self.cleaned_data['gapsma_prostate_suv']
        if gapsma_prostate_suv < 0:
            raise ValidationError('GA PSMA Prostate SUV must be a positive value')
        return gapsma_prostate_suv

    def clean_gapsma_prostate_size(self):
        gapsma_prostate_size = self.cleaned_data['gapsma_prostate_size']
        if gapsma_prostate_size < 0:
            raise ValidationError('GA PSMA Prostate Size must be a positive value')
        return gapsma_prostate_size

    def clean_gapsma_lymph_node_suv(self):
        gapsma_lymph_node_suv = self.cleaned_data['gapsma_lymph_node_suv']
        if gapsma_lymph_node_suv < 0:
            raise ValidationError('GA PSMA Lymph Node SUV must be a positive value')
        return gapsma_lymph_node_suv

    def clean_gapsma_lymph_node_size(self):
        gapsma_lymph_node_size = self.cleaned_data['gapsma_lymph_node_size']
        if gapsma_lymph_node_size < 0:
            raise ValidationError('GA PSMA Lymph Node Size must be a positive value')
        return gapsma_lymph_node_size

    def clean_gapsma_bone_suv(self):
        gapsma_bone_suv = self.cleaned_data['gapsma_bone_suv']
        if gapsma_bone_suv < 0:
            raise ValidationError('GA PSMA Bone SUV must be a positive value')
        return gapsma_bone_suv

    def clean_gapsma_bone_size(self):
        gapsma_bone_size = self.cleaned_data['gapsma_bone_size']
        if gapsma_bone_size < 0:
            raise ValidationError('GA PSMA Bone Size must be a positive value')
        return gapsma_bone_size

    def clean_gapsma_brain_suv(self):
        gapsma_brain_suv = self.cleaned_data['gapsma_brain_suv']
        if gapsma_brain_suv < 0:
            raise ValidationError('GA PSMA Brain SUV must be a positive value')
        return gapsma_brain_suv

    def clean_gapsma_brain_size(self):
        gapsma_brain_size = self.cleaned_data['gapsma_brain_size']
        if gapsma_brain_size < 0:
            raise ValidationError('GA PSMA Brain Size must be a positive value')
        return gapsma_brain_size

    def clean_gapsma_lung_suv(self):
        gapsma_lung_suv = self.cleaned_data['gapsma_lung_suv']
        if gapsma_lung_suv < 0:
            raise ValidationError('GA PSMA Lung SUV must be a positive value')
        return gapsma_lung_suv

    def clean_gapsma_lung_size(self):
        gapsma_lung_size = self.cleaned_data['gapsma_lung_size']
        if gapsma_lung_size < 0:
            raise ValidationError('GA PSMA Lung Size must be a positive value')
        return gapsma_lung_size

    def clean_gapsma_liver_suv(self):
        gapsma_liver_suv = self.cleaned_data['gapsma_liver_suv']
        if gapsma_liver_suv < 0:
            raise ValidationError('GA PSMA Liver SUV must be a positive value')
        return gapsma_liver_suv

    def clean_gapsma_liver_size(self):
        gapsma_liver_size = self.cleaned_data['gapsma_liver_size']
        if gapsma_liver_size < 0:
            raise ValidationError('GA PSMA Liver Size must be a positive value')
        return gapsma_liver_size

    def clean_fdgpetct_prostate_suv(self):
        fdgpetct_prostate_suv = self.cleaned_data['fdgpetct_prostate_suv']
        if fdgpetct_prostate_suv < 0:
            raise ValidationError('FDG PET CT Prostate SUV must be a positive value')
        return fdgpetct_prostate_suv

    def clean_fdgpetct_prostate_size(self):
        fdgpetct_prostate_size = self.cleaned_data['fdgpetct_prostate_size']
        if fdgpetct_prostate_size < 0:
            raise ValidationError('FDG PET CT Prostate Size must be a positive value')
        return fdgpetct_prostate_size

    def clean_fdgpetct_lymph_node_suv(self):
        fdgpetct_lymph_node_suv = self.cleaned_data['fdgpetct_lymph_node_suv']
        if fdgpetct_lymph_node_suv < 0:
            raise ValidationError('FDG PET CT Lymph Node SUV must be a positive value')
        return fdgpetct_lymph_node_suv

    def clean_fdgpetct_lymph_node_size(self):
        fdgpetct_lymph_node_size = self.cleaned_data['fdgpetct_lymph_node_size']
        if fdgpetct_lymph_node_size < 0:
            raise ValidationError('FDG PET CT Lymph Node Size must be a positive value')
        return fdgpetct_lymph_node_size

    def clean_fdgpetct_bone_suv(self):
        fdgpetct_bone_suv = self.cleaned_data['fdgpetct_bone_suv']
        if fdgpetct_bone_suv < 0:
            raise ValidationError('FDG PET CT Bone SUV must be a positive value')
        return fdgpetct_bone_suv

    def clean_fdgpetct_bone_size(self):
        fdgpetct_bone_size = self.cleaned_data['fdgpetct_bone_size']
        if fdgpetct_bone_size < 0:
            raise ValidationError('FDG PET CT Bone Size must be a positive value')
        return fdgpetct_bone_size

    def clean_fdgpetct_brain_suv(self):
        fdgpetct_brain_suv = self.cleaned_data['fdgpetct_brain_suv']
        if fdgpetct_brain_suv < 0:
            raise ValidationError('FDG PET CT Brain SUV must be a positive value')
        return fdgpetct_brain_suv

    def clean_fdgpetct_brain_size(self):
        fdgpetct_brain_size = self.cleaned_data['fdgpetct_brain_size']
        if fdgpetct_brain_size < 0:
            raise ValidationError('FDG PET CT Brain Size must be a positive value')
        return fdgpetct_brain_size

    def clean_fdgpetct_lung_suv(self):
        fdgpetct_lung_suv = self.cleaned_data['fdgpetct_lung_suv']
        if fdgpetct_lung_suv < 0:
            raise ValidationError('FDG PET CT Lung SUV must be a positive value')
        return fdgpetct_lung_suv

    def clean_fdgpetct_lung_size(self):
        fdgpetct_lung_size = self.cleaned_data['fdgpetct_lung_size']
        if fdgpetct_lung_size < 0:
            raise ValidationError('FDG PET CT Lung Size must be a positive value')
        return fdgpetct_lung_size

    def clean_fdgpetct_liver_suv(self):
        fdgpetct_liver_suv = self.cleaned_data['fdgpetct_liver_suv']
        if fdgpetct_liver_suv < 0:
            raise ValidationError('FDG PET CT Liver SUV must be a positive value')
        return fdgpetct_liver_suv

    def clean_fdgpetct_liver_size(self):
        fdgpetct_liver_size = self.cleaned_data['fdgpetct_liver_size']
        if fdgpetct_liver_size < 0:
            raise ValidationError('FDG PET CT Liver Size must be a positive value')
        return fdgpetct_liver_size

class EditScreening(forms.ModelForm):
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
        widgets = {
            'psa': forms.NumberInput(attrs={'step': 'any', 'min': '0'}),
            'creatinine': forms.NumberInput(attrs={'step': 'any', 'min': '0'}),
            'wbc': forms.NumberInput(attrs={'step': 'any', 'min': '0'}),
            'rbc': forms.NumberInput(attrs={'step': 'any', 'min': '0'}),
            'hemoglobin': forms.NumberInput(attrs={'step': 'any', 'min': '0'}),
            'hematocrit': forms.NumberInput(attrs={'step': 'any', 'min': '0'}),
            'platelet': forms.NumberInput(attrs={'step': 'any', 'min': '0'}),
            'lactate_hydrogenase': forms.NumberInput(attrs={'step': 'any', 'min': '0'}),
            'alkaline_phosphatase': forms.NumberInput(attrs={'step': 'any', 'min': '0'}),
            'sgpt': forms.NumberInput(attrs={'step': 'any', 'min': '0'}),
            'sgot': forms.NumberInput(attrs={'step': 'any', 'min': '0'}),
            'bilirubins': forms.NumberInput(attrs={'step': 'any', 'min': '0'}),
            'gapsma_prostate_suv': forms.NumberInput(attrs={'step': 'any', 'min': '0'}),
            'gapsma_prostate_size': forms.NumberInput(attrs={'step': 'any', 'min': '0'}),
            'gapsma_lymph_node_suv': forms.NumberInput(attrs={'step': 'any', 'min': '0'}),
            'gapsma_lymph_node_size': forms.NumberInput(attrs={'step': 'any', 'min': '0'}),
            'gapsma_bone_suv': forms.NumberInput(attrs={'step': 'any', 'min': '0'}),
            'gapsma_bone_size': forms.NumberInput(attrs={'step': 'any', 'min': '0'}),
            'gapsma_brain_suv': forms.NumberInput(attrs={'step': 'any', 'min': '0'}),
            'gapsma_brain_size': forms.NumberInput(attrs={'step': 'any', 'min': '0'}),
            'gapsma_lung_suv': forms.NumberInput(attrs={'step': 'any', 'min': '0'}),
            'gapsma_lung_size': forms.NumberInput(attrs={'step': 'any', 'min': '0'}),
            'gapsma_liver_suv': forms.NumberInput(attrs={'step': 'any', 'min': '0'}),
            'gapsma_liver_size': forms.NumberInput(attrs={'step': 'any', 'min': '0'}),
            'fdgpetct_prostate_suv': forms.NumberInput(attrs={'step': 'any', 'min': '0'}),
            'fdgpetct_prostate_size': forms.NumberInput(attrs={'step': 'any', 'min': '0'}),
            'fdgpetct_lymph_node_suv': forms.NumberInput(attrs={'step': 'any', 'min': '0'}),
            'fdgpetct_lymph_node_size': forms.NumberInput(attrs={'step': 'any', 'min': '0'}),
            'fdgpetct_bone_suv': forms.NumberInput(attrs={'step': 'any', 'min': '0'}),
            'fdgpetct_bone_size': forms.NumberInput(attrs={'step': 'any', 'min': '0'}),
            'fdgpetct_brain_suv': forms.NumberInput(attrs={'step': 'any', 'min': '0'}),
            'fdgpetct_brain_size': forms.NumberInput(attrs={'step': 'any', 'min': '0'}),
            'fdgpetct_lung_suv': forms.NumberInput(attrs={'step': 'any', 'min': '0'}),
            'fdgpetct_lung_size': forms.NumberInput(attrs={'step': 'any', 'min': '0'}),
            'fdgpetct_liver_suv': forms.NumberInput(attrs={'step': 'any', 'min': '0'}),
            'fdgpetct_liver_size': forms.NumberInput(attrs={'step': 'any', 'min': '0'}),
            'assessment': forms.Select(choices=Screening.ASSESSMENT, attrs={'required': True}),
            'plan': forms.Textarea(attrs={'required': True}),
        }