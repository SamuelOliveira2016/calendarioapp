# Generated by Django 4.0.10 on 2023-12-28 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0006_remove_cursounidadecurricularprofessor_professor_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='calendarioacademico',
            name='nome',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
