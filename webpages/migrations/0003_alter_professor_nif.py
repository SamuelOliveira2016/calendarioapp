# Generated by Django 4.0.10 on 2023-12-26 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0002_alter_professor_nif'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='nif',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
