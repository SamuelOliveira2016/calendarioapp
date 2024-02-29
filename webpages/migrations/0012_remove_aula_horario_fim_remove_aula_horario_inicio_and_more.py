# Generated by Django 4.0.10 on 2024-02-20 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0011_alter_cursounidadecurricularprofessor_curso_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aula',
            name='horario_fim',
        ),
        migrations.RemoveField(
            model_name='aula',
            name='horario_inicio',
        ),
        migrations.RemoveField(
            model_name='aula',
            name='infraestrutura',
        ),
        migrations.AddField(
            model_name='aula',
            name='infraestruturas',
            field=models.ManyToManyField(to='webpages.infraestrutura'),
        ),
    ]