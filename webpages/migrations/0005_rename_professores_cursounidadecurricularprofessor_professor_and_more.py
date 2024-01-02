# Generated by Django 4.0.10 on 2023-12-28 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0004_remove_cursounidadecurricularprofessor_curso'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cursounidadecurricularprofessor',
            old_name='professores',
            new_name='professor',
        ),
        migrations.RenameField(
            model_name='cursounidadecurricularprofessor',
            old_name='unidade_curricular',
            new_name='unidadeCurricular',
        ),
        migrations.AddField(
            model_name='cursounidadecurricularprofessor',
            name='curso',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='webpages.curso'),
        ),
    ]