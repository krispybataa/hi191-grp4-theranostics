from django.db import models
from part_1.models import *
from multiselectfield import MultiSelectField

# CLASS THERAPY ONLY SUPPORTS ONE ENTRY PER PATIENT AS OF NOW. OPTIMIZE LATER

class Therapy(models.Model):
    SIDE_EFFECTS = (
        ('Fatigue', 'Fatigue'),
        ('Nausea or Vomiting', 'Nausea or Vomiting'),
        ('Dry Lips or Mouth', 'Dry Lips or Mouth'),
        ('Headache', 'Headache'),
        ('Bone Pain', 'Bone Pain')
    )
    id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='t_patient')
    date_of_psma = models.DateField()
    premedications = models.CharField(max_length=120, null=True, blank=True)
    medications = models.CharField(max_length=120, null=True, blank=True)
    furosemide = models.BooleanField()
    systolic = models.IntegerField(blank=True, null=True)
    diastolic = models.IntegerField(blank=True, null=True)
    hr = models.IntegerField(blank=True, null=True)
    rr = models.IntegerField(blank=True, null=True)
    saturation = models.IntegerField(blank=True, null=True)
    date_therapy = models.DateField()
    radiopharm = models.CharField(max_length=120, null=True, blank=True)
    side_effects = MultiSelectField(choices=SIDE_EFFECTS, blank=True, null=True)
