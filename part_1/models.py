from django.db import models
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from django.template.defaultfilters import slugify
from datetime import datetime

class Patient(models.Model):
    TYPE_TREATMENT = (
        ('Hormonal Treatment', 'Hormonal Treatment'),
        ('Radiation Therapy', 'Radiation Therapy'),
        ('Chemotherapy', 'Chemotherapy'),
        ('Others', 'Others'),
    )
    #Test results and others are put to a different model
    name = models.CharField(max_length=120, blank= False, null=True)
    slug = models.SlugField(null=True)
    age = models.IntegerField()
    address = models.CharField(max_length=300)
    diagnosis_date = models.DateField()
    surgery_date = models.DateField()
    histopath_result = models.ImageField(upload_to="images/", blank=True, null=True)
    histopath_details = models.TextField(max_length=200, blank=False, null=True)
    gleason_score = models.IntegerField(blank=True, null=True)
    date_of_treatment = models.DateField()
    type_of_treatment = models.CharField(max_length=120, choices=TYPE_TREATMENT)

    def __str__(self): 
        return self.name

    #auto-add slugs
    def save(self, *args, **kwargs):  
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

class PhysicalExam(models.Model):
    id = models.AutoField(primary_key=True)
    date_recorded = models.DateField(default=datetime.now)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=True, null=True)
    ecog_score = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    bmi = models.DecimalField(max_digits=7, decimal_places=4, blank=True, null=True)
    bp = models.CharField(max_length=120, blank=True, null=True)
    hr = models.IntegerField(blank=True, null=True)
    pain_score = models.IntegerField(blank=True, null=True)
    local_symptoms = models.CharField(max_length=300, blank=True, null=True)
    systemic_symptoms = models.CharField(max_length=300, blank=True, null=True)


class Screening(models.Model):
    ASSESSMENT = (
        ('Low Risk', 'Low Risk'),
        ('Intermediate Risk', 'Intermediate Risk'),
        ('High Risk', 'High Risk'),
    )
    id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='screening_patient')
    psa = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    creatinine = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    wbc = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    rbc = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    hemoglobin = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    hematocrit = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    platelet = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    lactate_hydrogenase = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    alkaline_phosphatase = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    sgpt = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    sgot = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    bilirubins = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    SALIVARY_GLAND_STATUS = (
        ('Normal', 'Normal'),
        ('Left Obstruction', 'Left Obstruction'),
        ('Right Obstruction', 'Right Obstruction')
    )
    salivary_gland_status = models.CharField(max_length=120, choices=SALIVARY_GLAND_STATUS, blank=True, null=True)
    salivary_gland_image = models.ImageField(upload_to="images/", blank=True, null=True)

    BONE_METASTASIS_STATUS = (
        ('Metastasis', 'Metastasis'),
        ('No Metastasis', 'No Metastasis')
    )
    bone_metastasis_status = models.CharField(max_length=120, choices = BONE_METASTASIS_STATUS, blank=True, null=True)
    bone_scan_image = models.ImageField(upload_to="images/", null=True)
    renal_scintigraphy = models.ImageField(upload_to="images/")

    GAPSMA = (
        ('GA-68', 'GA-68'),
        ('F-18 PSMA', 'F-18 PSMA')
    )
    gapsma_choices = models.CharField(max_length=120, choices=GAPSMA, blank=True, null=True)
    gapsma_img = models.ImageField(upload_to="images/")

##THIS SEGMENT NEEDS OPTIMIZATION##
    # GAPSMA Lesions
    LESION_STATUS = (
        ('Absent', 'Absent'),
        ('Present', 'Present')
    )
    gapsma_prostate_lesion_status = models.CharField(verbose_name="Prostate Lesion Status", max_length=120, choices = LESION_STATUS, null=True, blank=True)
    gapsma_prostate_location = models.CharField(verbose_name="Prostate Location", max_length=50, null=True, blank=True)
    gapsma_prostate_suv = models.DecimalField(verbose_name="Prostate SUV", max_digits=5, decimal_places=2, blank=True, null=True)
    gapsma_prostate_size = models.IntegerField(verbose_name="Prostate Lesion Size", blank=True, null=True)

    gapsma_lymph_node_lesion_status = models.CharField(verbose_name="Lymph Node Lesion Status", max_length=120, choices = LESION_STATUS, null=True, blank=True)
    gapsma_lymph_node_location = models.CharField(verbose_name="Lymph Node Location", max_length=50, null=True, blank=True)
    gapsma_lymph_node_suv = models.DecimalField(verbose_name="Lymph Node SUV", max_digits=5, decimal_places=2, blank=True, null=True)
    gapsma_lymph_node_size = models.IntegerField(verbose_name="Lymph Node Lesion Size", blank=True, null=True)

    gapsma_bone_lesion_status = models.CharField(verbose_name="Bone Lesion Status", max_length=120, choices = LESION_STATUS, null=True, blank=True)
    gapsma_bone_location = models.CharField(verbose_name="Bone Lesion Location", max_length=50, null=True, blank=True)
    gapsma_bone_suv = models.DecimalField(verbose_name="Bone SUV", max_digits=5, decimal_places=2, blank=True, null=True)
    gapsma_bone_size = models.IntegerField(verbose_name="Bone Lesion Size", blank=True, null=True)

    gapsma_brain_lesion_status = models.CharField(verbose_name="Brain Lesion Status", max_length=120, choices = LESION_STATUS, null=True, blank=True)
    gapsma_brain_location = models.CharField(verbose_name="Brain Lesion Location", max_length=50, null=True, blank=True)
    gapsma_brain_suv = models.DecimalField(verbose_name="Brain SUV", max_digits=5, decimal_places=2, blank=True, null=True)
    gapsma_brain_size = models.IntegerField(verbose_name="Brain Lesion Size", blank=True, null=True)

    gapsma_lung_lesion_status = models.CharField(verbose_name="Lung Lesion Status", max_length=120, choices = LESION_STATUS, null=True, blank=True)
    gapsma_lung_location = models.CharField(verbose_name="Lung Lesion Location", max_length=50, null=True, blank=True)
    gapsma_lung_suv = models.DecimalField(verbose_name="Lung SUV", max_digits=5, decimal_places=2, blank=True, null=True)
    gapsma_lung_size = models.IntegerField(verbose_name="Lung Lesion Size", blank=True, null=True)

    gapsma_liver_lesion_status = models.CharField(verbose_name="Liver Lesion Status", max_length=120, choices = LESION_STATUS, null=True, blank=True)
    gapsma_liver_location = models.CharField(verbose_name="Liver Lesion Location", max_length=50, null=True, blank=True)
    gapsma_liver_suv = models.DecimalField(verbose_name="Liver SUV", max_digits=5, decimal_places=2, blank=True, null=True)
    gapsma_liver_size = models.IntegerField(verbose_name="Liver Lesion Size", blank=True, null=True)

    fdgpetct_img = models.ImageField(upload_to="images/")

    # For fdgpetct

    fdgpetct_prostate_lesion_status = models.CharField(verbose_name="Prostate Lesion Status", max_length=120, choices = LESION_STATUS, null=True, blank=True)
    fdgpetct_prostate_location = models.CharField(verbose_name="Prostate Location", max_length=50, null=True, blank=True)
    fdgpetct_prostate_suv = models.DecimalField(verbose_name="Prostate SUV", max_digits=5, decimal_places=2, blank=True, null=True)
    fdgpetct_prostate_size = models.IntegerField(verbose_name="Prostate Lesion Size", blank=True, null=True)

    fdgpetct_lymph_node_lesion_status = models.CharField(verbose_name="Lymph Node Lesion Status", max_length=120, choices = LESION_STATUS, null=True, blank=True)
    fdgpetct_lymph_node_location = models.CharField(verbose_name="Lymph Node Location", max_length=50, null=True, blank=True)
    fdgpetct_lymph_node_suv = models.DecimalField(verbose_name="Lymph Node SUV", max_digits=5, decimal_places=2, blank=True, null=True)
    fdgpetct_lymph_node_size = models.IntegerField(verbose_name="Lymph Node Lesion Size", blank=True, null=True)

    fdgpetct_bone_lesion_status = models.CharField(verbose_name="Bone Lesion Status", max_length=120, choices = LESION_STATUS, null=True, blank=True)
    fdgpetct_bone_location = models.CharField(verbose_name="Bone Lesion Location", max_length=50, null=True, blank=True)
    fdgpetct_bone_suv = models.DecimalField(verbose_name="Bone SUV", max_digits=5, decimal_places=2, blank=True, null=True)
    fdgpetct_bone_size = models.IntegerField(verbose_name="Bone Lesion Size", blank=True, null=True)

    fdgpetct_brain_lesion_status = models.CharField(verbose_name="Brain Lesion Status", max_length=120, choices = LESION_STATUS, null=True, blank=True)
    fdgpetct_brain_location = models.CharField(verbose_name="Brain Lesion Location", max_length=50, null=True, blank=True)
    fdgpetct_brain_suv = models.DecimalField(verbose_name="Brain SUV", max_digits=5, decimal_places=2, blank=True, null=True)
    fdgpetct_brain_size = models.IntegerField(verbose_name="Brain Lesion Size", blank=True, null=True)

    fdgpetct_lung_lesion_status = models.CharField(verbose_name="Lung Lesion Status", max_length=120, choices = LESION_STATUS, null=True, blank=True)
    fdgpetct_lung_location = models.CharField(verbose_name="Lung Lesion Location", max_length=50, null=True, blank=True)
    fdgpetct_lung_suv = models.DecimalField(verbose_name="Lung SUV", max_digits=5, decimal_places=2, blank=True, null=True)
    fdgpetct_lung_size = models.IntegerField(verbose_name="Lung Lesion Size", blank=True, null=True)

    fdgpetct_liver_lesion_status = models.CharField(verbose_name="Liver Lesion Status", max_length=120, choices = LESION_STATUS, null=True, blank=True)
    fdgpetct_liver_location = models.CharField(verbose_name="Liver Lesion Location", max_length=50, null=True, blank=True)
    fdgpetct_liver_suv = models.DecimalField(verbose_name="Liver SUV", max_digits=5, decimal_places=2, blank=True, null=True)
    fdgpetct_liver_size = models.IntegerField(verbose_name="Liver Lesion Size", blank=True, null=True)

    assessment = models.TextField(blank=True, null=True)
    plan = models.TextField(blank=True, null=True)
 