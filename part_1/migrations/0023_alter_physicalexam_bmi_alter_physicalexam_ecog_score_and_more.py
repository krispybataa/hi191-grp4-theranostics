# Generated by Django 4.2.5 on 2025-01-07 05:04

from django.db import migrations, models
import part_1.models


class Migration(migrations.Migration):

    dependencies = [
        ('part_1', '0022_alter_physicalexam_bmi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='physicalexam',
            name='bmi',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, validators=[part_1.models.validate_positive]),
        ),
        migrations.AlterField(
            model_name='physicalexam',
            name='ecog_score',
            field=models.IntegerField(blank=True, null=True, validators=[part_1.models.validate_positive]),
        ),
        migrations.AlterField(
            model_name='physicalexam',
            name='height',
            field=models.IntegerField(blank=True, null=True, validators=[part_1.models.validate_positive]),
        ),
        migrations.AlterField(
            model_name='physicalexam',
            name='hr',
            field=models.IntegerField(blank=True, null=True, validators=[part_1.models.validate_positive]),
        ),
        migrations.AlterField(
            model_name='physicalexam',
            name='pain_score',
            field=models.IntegerField(blank=True, null=True, validators=[part_1.models.validate_positive]),
        ),
        migrations.AlterField(
            model_name='physicalexam',
            name='weight',
            field=models.IntegerField(blank=True, null=True, validators=[part_1.models.validate_positive]),
        ),
        migrations.AlterField(
            model_name='screening',
            name='alkaline_phosphatase',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='screening',
            name='assessment',
            field=models.CharField(blank=True, choices=[('Low Risk', 'Low Risk'), ('Intermediate Risk', 'Intermediate Risk'), ('High Risk', 'High Risk')], max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='screening',
            name='bilirubins',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='screening',
            name='bone_scan_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='screening',
            name='creatinine',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='screening',
            name='fdgpetct_bone_lesion_status',
            field=models.CharField(blank=True, choices=[('Absent', 'Absent'), ('Present', 'Present')], max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='screening',
            name='fdgpetct_bone_location',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='screening',
            name='fdgpetct_bone_size',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='screening',
            name='fdgpetct_bone_suv',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='screening',
            name='fdgpetct_brain_lesion_status',
            field=models.CharField(blank=True, choices=[('Absent', 'Absent'), ('Present', 'Present')], max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='screening',
            name='fdgpetct_brain_location',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='screening',
            name='fdgpetct_brain_size',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='screening',
            name='fdgpetct_brain_suv',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='screening',
            name='fdgpetct_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='screening',
            name='fdgpetct_liver_lesion_status',
            field=models.CharField(blank=True, choices=[('Absent', 'Absent'), ('Present', 'Present')], max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='screening',
            name='fdgpetct_liver_location',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='screening',
            name='fdgpetct_liver_size',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='screening',
            name='fdgpetct_liver_suv',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='screening',
            name='fdgpetct_lung_lesion_status',
            field=models.CharField(blank=True, choices=[('Absent', 'Absent'), ('Present', 'Present')], max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='screening',
            name='fdgpetct_lung_location',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='screening',
            name='fdgpetct_lung_size',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='screening',
            name='fdgpetct_lung_suv',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='screening',
            name='fdgpetct_lymph_node_lesion_status',
            field=models.CharField(blank=True, choices=[('Absent', 'Absent'), ('Present', 'Present')], max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='screening',
            name='fdgpetct_lymph_node_location',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='screening',
            name='fdgpetct_lymph_node_size',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='screening',
            name='fdgpetct_lymph_node_suv',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='screening',
            name='fdgpetct_prostate_lesion_status',
            field=models.CharField(blank=True, choices=[('Absent', 'Absent'), ('Present', 'Present')], max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='screening',
            name='fdgpetct_prostate_location',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='screening',
            name='fdgpetct_prostate_size',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='screening',
            name='fdgpetct_prostate_suv',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='screening',
            name='gapsma_bone_lesion_status',
            field=models.CharField(blank=True, choices=[('Absent', 'Absent'), ('Present', 'Present')], max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='screening',
            name='gapsma_bone_location',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='screening',
            name='gapsma_bone_size',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='screening',
            name='gapsma_bone_suv',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='screening',
            name='gapsma_brain_lesion_status',
            field=models.CharField(blank=True, choices=[('Absent', 'Absent'), ('Present', 'Present')], max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='screening',
            name='gapsma_brain_location',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='screening',
            name='gapsma_brain_size',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='screening',
            name='gapsma_brain_suv',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='screening',
            name='gapsma_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='screening',
            name='gapsma_liver_lesion_status',
            field=models.CharField(blank=True, choices=[('Absent', 'Absent'), ('Present', 'Present')], max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='screening',
            name='gapsma_liver_location',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='screening',
            name='gapsma_liver_size',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='screening',
            name='gapsma_liver_suv',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='screening',
            name='gapsma_lung_lesion_status',
            field=models.CharField(blank=True, choices=[('Absent', 'Absent'), ('Present', 'Present')], max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='screening',
            name='gapsma_lung_location',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='screening',
            name='gapsma_lung_size',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='screening',
            name='gapsma_lung_suv',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='screening',
            name='gapsma_lymph_node_lesion_status',
            field=models.CharField(blank=True, choices=[('Absent', 'Absent'), ('Present', 'Present')], max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='screening',
            name='gapsma_lymph_node_location',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='screening',
            name='gapsma_lymph_node_size',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='screening',
            name='gapsma_lymph_node_suv',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='screening',
            name='gapsma_prostate_lesion_status',
            field=models.CharField(blank=True, choices=[('Absent', 'Absent'), ('Present', 'Present')], max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='screening',
            name='gapsma_prostate_location',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='screening',
            name='gapsma_prostate_size',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='screening',
            name='gapsma_prostate_suv',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='screening',
            name='hematocrit',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='screening',
            name='hemoglobin',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='screening',
            name='lactate_hydrogenase',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='screening',
            name='plan',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='screening',
            name='platelet',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='screening',
            name='psa',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='screening',
            name='rbc',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='screening',
            name='renal_scintigraphy',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='screening',
            name='sgot',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='screening',
            name='sgpt',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='screening',
            name='wbc',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True),
        ),
    ]
