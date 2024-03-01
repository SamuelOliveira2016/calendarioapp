# Generated by Django 4.0.10 on 2024-03-01 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0032_infraestrutura_cor_alter_infraestrutura_tipo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='areatecnologica',
            options={'ordering': ['descricao']},
        ),
        migrations.RemoveField(
            model_name='areatecnologica',
            name='nome',
        ),
        migrations.AlterField(
            model_name='areatecnologica',
            name='descricao',
            field=models.CharField(max_length=255),
        ),
    ]