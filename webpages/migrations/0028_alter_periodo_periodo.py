# Generated by Django 4.0.10 on 2024-03-01 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0027_periodo_delete_horatrabprof'),
    ]

    operations = [
        migrations.AlterField(
            model_name='periodo',
            name='periodo',
            field=models.CharField(choices=[('Manhã', 'manhã'), ('Tarde', 'tarde'), ('Noite', 'noite'), ('Integral', 'integral')], max_length=8),
        ),
    ]