# Generated by Django 4.0.10 on 2023-12-08 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Areatecnologica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Calendario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diasLetivos', models.IntegerField()),
                ('feriados', models.DateField(blank=True, null=True)),
                ('pontes', models.DateField(blank=True, null=True)),
                ('periodo', models.CharField(choices=[('manhã', 'Manhã'), ('tarde', 'Tarde'), ('noite', 'Noite')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='HoratrabProf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horariotrabalho', models.TimeField()),
                ('diastrabalho', models.IntegerField()),
                ('quantmes', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Infra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salaula', models.BooleanField(default=False)),
                ('lab', models.BooleanField(default=False)),
                ('oficina', models.BooleanField(default=False)),
                ('capacid', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('telefone', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Planocurso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomecurso', models.CharField(max_length=255)),
                ('modulo', models.IntegerField()),
                ('unidadecurricular', models.CharField(max_length=255)),
                ('carcahorauc', models.IntegerField()),
                ('competenciastecnicas', models.TextField()),
                ('competenciasSOM', models.TextField()),
                ('conhecimentos', models.TextField()),
                ('areatecnologica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webpages.areatecnologica')),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nif', models.CharField(max_length=15, unique=True)),
                ('cargonivel', models.CharField(max_length=255)),
                ('listunidcurri', models.ManyToManyField(to='webpages.planocurso')),
            ],
        ),
        migrations.CreateModel(
            name='Tipocurso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('cursolivre', 'Curso Livre'), ('cursoregular', 'Curso Regular'), ('cursoFic', 'Curso FIC')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Vinculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horista', models.BooleanField(choices=[('horista', 'Horista'), ('prazo_indeter', 'Prazo Indeterminado'), ('temporario', 'Temporário')])),
                ('prazo_indeter', models.BooleanField(choices=[('horista', 'Horista'), ('prazo_indeter', 'Prazo Indeterminado'), ('temporario', 'Temporário')])),
                ('temporario', models.BooleanField(choices=[('horista', 'Horista'), ('prazo_indeter', 'Prazo Indeterminado'), ('temporario', 'Temporário')])),
                ('prazoDeter', models.DateField()),
                ('horatrabProf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webpages.horatrabprof')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webpages.pessoa')),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.AddField(
            model_name='planocurso',
            name='tipocurso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webpages.tipocurso'),
        ),
        migrations.AddField(
            model_name='infra',
            name='professor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webpages.professor'),
        ),
        migrations.AddField(
            model_name='infra',
            name='tipocurso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webpages.tipocurso'),
        ),
        migrations.AddField(
            model_name='calendario',
            name='infra',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webpages.infra'),
        ),
        migrations.AddField(
            model_name='calendario',
            name='professor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webpages.professor'),
        ),
        migrations.AddField(
            model_name='calendario',
            name='tipocurso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webpages.tipocurso'),
        ),
    ]