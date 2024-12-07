# Generated by Django 5.1.1 on 2024-12-06 19:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_materia', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=200)),
                ('especialidade', models.CharField(max_length=100)),
                ('horario_disponibilidade', models.CharField(max_length=100)),
                ('contato_telefone', models.CharField(max_length=15)),
                ('contato_email', models.EmailField(max_length=254)),
                ('endereco', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_turma', models.CharField(max_length=50)),
                ('ano', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Atribuicao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio', models.DateField()),
                ('data_fim', models.DateField()),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.materia')),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.professor')),
                ('turma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.turma')),
            ],
        ),
    ]