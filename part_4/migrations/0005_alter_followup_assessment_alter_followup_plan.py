# Generated by Django 4.2.5 on 2025-01-05 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('part_4', '0004_alter_followup_patient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followup',
            name='assessment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='followup',
            name='plan',
            field=models.TextField(blank=True, null=True),
        ),
    ]
