# Generated by Django 5.1.1 on 2024-12-07 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_atribuicao_data_fim_alter_atribuicao_professor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turma',
            name='turno',
            field=models.CharField(choices=[('I', 'Integral'), ('M', 'Manhã'), ('T', 'Tarde'), ('N', 'Noite')], max_length=1),
        ),
    ]
